from odoo import  models , fields


class Tag (models.Model):
    _name = 'tag'
    _description = 'tag Description'

    name = fields.Char(required=True)
