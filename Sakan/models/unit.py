from odoo import  models , fields


class Unit (models.Model):
    _name = 'unit'
    _description = 'Unit'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    type= fields.Selection([
        ('old','Old House'),
        ('new','New House'),
        ])
    university =fields.Many2one('university')
