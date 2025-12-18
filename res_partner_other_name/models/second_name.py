from odoo import models, fields

class SecondName(models.Model):
    _name = 'second.name'
    _description = 'Second Name'

    name = fields.Char(string="Second Name", required=True)
    partner_id = fields.Many2one('res.partner', string="Customer")
