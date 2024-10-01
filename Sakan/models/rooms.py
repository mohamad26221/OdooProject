from odoo import models, fields, api


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
    student_ids = fields.One2many('student', 'room')
    student_count = fields.Integer(string="عدد الطلاب", compute='_compute_student_count')

    @api.depends('student_ids')
    def _compute_student_count(self):
        for room in self:
            room.student_count = len(room.student_ids)
            if room.student_count == 0:
                room.state = 'empty'
            elif 0 < room.student_count < 3:
                room.state = 'available'
            elif room.student_count >= 3:
                room.state = 'unavailable'

    def action_empty(self):
        for rec in self:
            rec.state = 'empty'
            rec.student_count = 0
            students = self.env['student'].search([('room', '=', rec.id)])
            for student in students:
                student.room = False


