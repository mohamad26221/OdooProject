from odoo import fields , models




class ChangeState(models.TransientModel):
    _name = 'change.state'
    _description = 'change_state'

    room_id= fields.Many2one('rooms')
    state = fields.Selection([
        ('empty','Empty'),
        ('available','Available'),
        ('full','Full'),
    ],default='empty')
    reason = fields.Char()


    def action_confirm(self):
        if self.room_id.state == 'broken':
            self.room_id.state = self.state
            self.room_id.create_history_record('broken',self.state, self.reason)