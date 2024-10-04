from odoo import models, fields, api


class Rooms (models.Model):
    _name = 'rooms'
    _description = 'Room'
    # _rec_name = 'name'

    name = fields.Char(required=True)
    floor = fields.Char()
    active = fields.Boolean(default=True)
    state= fields.Selection([
        ('empty','Empty'),
        ('available','Available'),
        ('full','Full'),
        ])
    unit = fields.Many2one('unit')
    student_ids = fields.One2many('student', 'room')
    student_count = fields.Integer(compute='_compute_student_count')

    @api.depends('student_ids')
    def _compute_student_count(self):
        for room in self:
            room.student_count = len(room.student_ids)
            if room.student_count == 0:
                room.state = 'empty'
            elif 0 < room.student_count < 3:
                room.state = 'available'
            elif room.student_count >= 3:
                room.state = 'full'

    def action_empty(self):
        for rec in self:
            rec.state = 'empty'
            rec.student_count = 0
            students = self.env['student'].search([('room', '=', rec.id)])
            for student in students:
                student.room = False


