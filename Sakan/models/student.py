from odoo import models, fields, api, exceptions


class Student(models.Model):
    _name = 'student'
    _description = 'student Description'

    name = fields.Char(required=True,string="اسم الطالب")
    email = fields.Char(string="البريد الالكتروني", required=True)
    father_name = fields.Char(string="اسم الاب")
    last_name = fields.Char(string="الكنية")
    phone = fields.Char(string="رقم الموبايل", required=True)
    section = fields.Char(string="الاختصاص")
    unit= fields.Many2one('unit',string="الوحدة")
    room= fields.Many2one('rooms',string="الغرفة")
    university= fields.Many2one('university',string="الجامعة")

    _sql_constraints = [
        ('unique_name','unique("email")','the email is exist!'),
        ('unique_name','unique("phone")','the phone is exist!'),
    ]
    @api.constrains('room')
    def _check_room_capacity(self):
        for student in self:
            if student.room and len(student.room.student_ids) > 3:
                raise exceptions.ValidationError("الغرفة ممتلئة لا يمكن اضافة المزيد من الطلاب")