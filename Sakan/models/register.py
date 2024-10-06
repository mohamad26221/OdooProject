from odoo import models, fields, api, exceptions


class Register(models.Model):
    _name = 'register'
    _description = 'Register Student'
    _inherit = ['student']

    student_id = fields.Many2one('student')
    name = fields.Char(related='student_id.name')
    number = fields.Char(default='new',readonly=True)
    unit= fields.Many2one(related='student_id.unit')
    room= fields.Many2one(related='student_id.room')
    university= fields.Many2one(related='student_id.university')
    front_face = fields.Binary(string="Front Face", attachment=True)
    back_face = fields.Binary(string="Back Face", attachment=True)
    face_picture = fields.Binary(string="Face Picture", attachment=True)
    payment_method = fields.Selection([
        ('syriatel','SyriatelCash'),
        ('mtn','MtnCash'),
        ('bemo','Bemo'),
        ])
    expected_payment = fields.Date(string="Expected Payment", tracking=True, default='2024-10-03')
    is_late= fields.Boolean()
    state= fields.Selection([
        ('accepted','Accepted'),
        ('waiting','Waiting'),
        ('rejected','Rejected'),
        ],default='rejected')
    def check_expected_payment(self):
        register_ids = self.search([])
        for rec in register_ids :
            if rec.expected_payment and rec.expected_payment < fields.date.today():
                rec.is_late = True
    @api.model
    def create(self, vals):
        res = super(Register,self).create(vals)
        if res.number == 'new':
            res.number = self.env['ir.sequence'].next_by_code('register_sec')
        return  res
