from odoo import models, fields , api


class Children(models.Model):
    _name = 'children'
    _description = 'Children'

    name = fields.Char(string='Child Name', required=True)
    birthdate = fields.Date(string="Birthdate", required=True)
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)


    @api.model
    def get_children_statistics(self):
        total_children = self.search_count([])
        calculated_children = self.search_count([('calculated_score', '!=', False)])
        return {
            'total': total_children,
            'calculated': calculated_children
        }