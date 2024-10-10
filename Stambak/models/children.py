from odoo import models, fields


class Children(models.Model):
    _name = 'children'
    _description = 'Children'

    name = fields.Char(string='Child Name', required=True)
    birthdate = fields.Date(string="Birthdate", required=True)
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
