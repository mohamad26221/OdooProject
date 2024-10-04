from odoo import  models , fields

class University (models.Model):
    _name = 'university'
    _description = 'University'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    city= fields.Selection([
        ('tartous','Tartous'),
        ('lattakia','Lattakia'),
        ('homs','Homs'),
        ('damascous','Damascous'),
        ('aleepo','Aleepo'),
        ])