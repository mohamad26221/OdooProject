from odoo import models , fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    student_id = fields.Many2one('student')

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm() 
        print("inside action confirm method")
        return res
