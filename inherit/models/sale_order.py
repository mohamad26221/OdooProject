from odoo import models, fields , api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_purchase_count = fields.Integer(
        string='Customer Purchase Count',
        compute='_compute_customer_purchase_count'
    )

    @api.onchange('partner_id')
    def _compute_customer_purchase_count(self):
        for order in self:
            if order.partner_id:
                order.customer_purchase_count = self.env['sale.order'].search_count([
                    ('partner_id', '=', order.partner_id.id),
                    ('state', 'in', ['sale', 'done'])
                ])
            else:
                order.customer_purchase_count = 0
