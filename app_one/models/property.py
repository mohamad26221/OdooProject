from docutils.core import default_usage

from odoo import  models , fields ,api
from odoo.exceptions import ValidationError


class Property (models.Model):
    _name = 'property'
    _description = 'Property Description'

    name = fields.Char(required=True , default='mohamd', size=6)
    description = fields.Text()
    postcode = fields.Char(required=True)
    data_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float(digits=(0,5))
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garage_area = fields.Integer()
    garage_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
        ])
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    state = fields.Selection([
            ('draft','Draft'),
            ('pending','Pending'),
            ('sold','Sold'),
    ],default='draft')

    _sql_constraints = [
        ('unique_name','unique("name")','the name is exist!')
    ]
    @api.constrains('bedrooms')
    def _check_bedrooms_creator_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError('please add valid number of field (Bedrooms).')

    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        print("inside create")
        return res
    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(Property, self)._search( domain, offset=0, limit=None, order=None, access_rights_uid=None)
        print("inside search")
        return res
    def write(self, vals):
        res = super(Property, self).write(vals)
        print("inside write")
        return res
    def unlink(self):
        res = super(Property, self).unlink()
        print("inside delete")
        return res