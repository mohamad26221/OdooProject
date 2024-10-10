from odoo import models, fields


class Tests(models.Model):
    _name = 'tests'
    _description = 'Tests'
    _rec_name = 'test_name'


    test_name = fields.Char(string='Test Name', required=True)
    description = fields.Text(string='Description')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
