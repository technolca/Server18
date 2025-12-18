from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    second_name = fields.Many2one('second.name',string="Second Name", index=True, tracking=True)
