from datetime import datetime
from odoo.exceptions import UserError
from odoo import models, fields, api


class Results(models.Model):
    _name = 'results'
    _description = 'Results'

    child_id = fields.Many2one('children', string='Child', required=True, ondelete='cascade')
    test_id = fields.Many2one('tests', string='Test')
    raw_score = fields.Float(string='Raw Score', required=True, digits=(2, 1))
    child_age = fields.Integer(string="Child Age", compute="_compute_child_age", store=True)
    calculated_score = fields.Float(string='Calculated Score', compute='_compute_calculated_score', store=True)
    category = fields.Selection([
        ('within', 'Within the normal'),
        ('above', 'Above the normal'),
        ('below', 'Below the normal'),
        ('difficulty', 'Difficulty limits'),
    ], string='Category')

    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)

    @api.depends('child_id')
    def _compute_child_age(self):
        for record in self:
            if record.child_id and record.child_id.birthdate:
                today = datetime.today()
                birthdate = fields.Date.from_string(record.child_id.birthdate)

                years_difference = today.year - birthdate.year
                months_difference = today.month - birthdate.month

                if months_difference < 0:
                    months_difference += 12

                if months_difference >= 6:
                    years_difference += 1

                record.child_age = years_difference
            else:
                record.child_age = 0

    @api.depends('raw_score','test_id')
    def _compute_calculated_score(self):
        for record in self:
            if record.test_id and record.child_age:
                mean, standard_deviation = self._get_mean_and_std(record.child_age, record.test_id)
                record.calculated_score = (record.raw_score - mean) / standard_deviation

                if -1 <= record.calculated_score <= 1:
                    record.category = 'within'
                elif -2 <= record.calculated_score < -1 or 1 < record.calculated_score <= 2:
                    record.category = 'above'
                elif record.calculated_score < -2:
                    record.category = 'below'
                elif record.calculated_score > 2:
                    record.category = 'difficulty'
                else:
                    record.calculated_score = 0.0
                    record.category = 'within'
            else:
                record.calculated_score = 0.0
                record.category = 'within'

    def _get_mean_and_std(self, age, test_id):
        if test_id:
            reference_record = self.env['reference'].search([
                ('age_group', '=', age),
                ('test_id', '=', test_id.id)
            ], limit=1)

            if reference_record:
                return reference_record.mean_score, reference_record.std_deviation
        return 0.0, 0.0

    def action_show_result_popup(self):
        self.ensure_one()

        if not self.calculated_score:
            raise UserError("لم يتم حساب النتيجة بعد!")

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'results',
            'view_mode': 'form',
            'res_id': self.id,
            'views': [(self.env.ref('Stambak.view_results_popup_form').id, 'form')],
            'target': 'new',
        }
