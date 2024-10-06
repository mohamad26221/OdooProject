from odoo import models, fields, api, exceptions


class Student(models.Model):
    _name = 'student'
    _description = 'Student'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(required=True)
    email = fields.Char()
    father_name = fields.Char()
    last_name = fields.Char()
    phone = fields.Char()
    section = fields.Char()
    birthday = fields.Date(tracking=True)
    unit= fields.Many2one('unit')
    room= fields.Many2one('rooms',tracking=True)
    room_floor = fields.Char(related='room.floor')
    university= fields.Many2one('university')
    StudentStudy_ids= fields.One2many('student.study','student_id')
    city = fields.Selection(related='university.city')
    active = fields.Boolean(default=True)
    register_ids = fields.One2many('register','student_id')

    _sql_constraints = [
        ('unique_name','unique("email")','the email is exist!'),
        ('unique_name','unique("phone")','the phone is exist!'),
    ]
    @api.constrains('room')
    def _check_room_capacity(self):
        for student in self:
            if student.room and len(student.room.student_ids) > 3 :
                raise exceptions.ValidationError("Room is full")

class StudentStudy(models.Model):
    _name = 'student.study'
    _description = 'Study Information'
    
    student_id= fields.Many2one('student')
    College = fields.Char()
    Specialization= fields.Char()