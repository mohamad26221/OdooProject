from odoo import  models , fields ,api


class Rooms (models.Model):
    _name = 'rooms'
    _description = 'rooms Description'

    name = fields.Char(string="رقم الغرفة", required=True)
    floor = fields.Char(string="الطابق")
    state= fields.Selection([
        ('empty','فارغة'),
        ('available','متاحة'),
        ('unavailable','ممتلئة'),
        ],string="حالة الغرفة")
    unit = fields.Many2one('unit',string="الوحدة")
    student_count = fields.Integer(string="عدد الطلاب", compute='_compute_student_count')

    @api.depends()
    def _compute_student_count(self):
        for room in self:
            room.student_count = self.env['student'].search_count([('room', '=', room.id)])