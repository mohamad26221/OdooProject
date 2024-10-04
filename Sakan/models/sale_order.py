from odoo import models , fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    student_id = fields.Many2one('student')
    phone = fields.Char(related='student_id.phone')
    room = fields.Many2one(related='student_id.room')
    student_count = fields.Integer(related='student_id.room.student_count')


    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm() 
        print("inside action confirm method")
        return res
