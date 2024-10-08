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
        ('broken','Broken'),
        ])
    unit = fields.Many2one('unit')
    student_ids = fields.One2many('student', 'room')
    student_count = fields.Integer(compute='_compute_student_count')

    @api.depends('student_ids')
    def _compute_student_count(self):
        for room in self:
            room.student_count = len(room.student_ids)
            if 0 < room.student_count < 3:
                room.state = 'available'
            elif room.student_count >= 3:
                room.state = 'full'


    def action_empty(self):
        for rec in self:
            rec.create_history_record(rec.state, 'empty','')
            rec.state = 'empty'
            rec.student_count = 0
            students = self.env['student'].search([('room', '=', rec.id)])
            for student in students:
                student.room = False
    def action_broken(self):
        for rec in self:
            rec.create_history_record(rec.state,'broken',' ')
            rec.state = 'broken'


    def create_history_record(self,old_state,new_state, reason):
        for rec in self:
            rec.env['room.history'].create({
                'user_id': rec.env.uid,
                'room_id': rec.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason or "",
            })
    def action_open_change_state_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('Sakan.change_state_wizard_action')
        action['context'] = {'default_room_id':self.id}
        return action



class RoomHistory(models.Model):
    _name = 'room.history'
    _description = 'Room History'

    user_id = fields.Many2one('res.users')
    room_id = fields.Many2one('rooms')
    old_state = fields.Char()
    new_state = fields.Char()
    reason = fields.Char()