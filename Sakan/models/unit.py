from odoo import  models , fields


class Unit (models.Model):
    _name = 'unit'
    _description = 'unit Description'

    name = fields.Char(required=True , default='الوحدة' , string='اسم الوحدة')
    type= fields.Selection([
        ('old','سكن قديم'),
        ('new','سكن جديد'),
        ],string='نوعها')
    university =fields.Many2one('university',string='موجودة في ')
