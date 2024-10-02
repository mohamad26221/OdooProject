from odoo import models, fields, api, exceptions


class Student(models.Model):
    _name = 'student'
    _description = 'student Description'

    name = fields.Char(required=True)
    email = fields.Char( required=True)
    father_name = fields.Char()
    last_name = fields.Char()
    phone = fields.Char( required=True)
    section = fields.Char()
    unit= fields.Many2one('unit')
    room= fields.Many2one('rooms')
    university= fields.Many2one('university')

    _sql_constraints = [
        ('unique_name','unique("email")','the email is exist!'),
        ('unique_name','unique("phone")','the phone is exist!'),
    ]
    @api.constrains('room')
    def _check_room_capacity(self):
        for student in self:
            if student.room and len(student.room.student_ids) > 3:
                raise exceptions.ValidationError("الغرفة ممتلئة لا يمكن اضافة المزيد من الطلاب")