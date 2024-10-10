from odoo import models, fields


class Reference(models.Model):
    _name = 'reference'
    _description = 'Reference'

    test_id = fields.Many2one('tests', string='Test', required=True)
    age_group = fields.Integer(string='Age Group', required=True)
    mean_score = fields.Float(string='Mean Score', required=True, digits=(2, 1))
    std_deviation = fields.Float(string='Standard Deviation', required=True, digits=(2, 1))
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
