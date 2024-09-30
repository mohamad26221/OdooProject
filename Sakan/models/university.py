from odoo import  models , fields ,api


class University (models.Model):
    _name = 'university'
    _description = 'University Description'

    name = fields.Char(required=True, default='جامعة',string="اسم الجامعة")
    city= fields.Selection([
        ('tartous','طرطوس'),
        ('lattakia','اللاذقية'),
        ('homs','حمص'),
        ('damascous','دمشق'),
        ('aleepo','حلب'),
        ],string="المدينة")