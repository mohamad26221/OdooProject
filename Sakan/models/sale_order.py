from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm() #now
        print("inside action confirm method")
        return res
