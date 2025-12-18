from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'crm.lead'

    partner_second_name = fields.Many2one(
        'second.name',
        string="Second Name",
        compute='_compute_partner_second_name',
        store=True,
        index=True,
        readonly=False
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        compute='_compute_partner_second_name',
        store=True,
        readonly=False
    )

    @api.depends('partner_id')
    def _compute_partner_second_name(self):
        for record in self:
            record.partner_second_name = record.partner_id.second_name if record.partner_id else ''

    @api.onchange('partner_second_name')
    def _onchange_partner_second_name(self):
        if self.partner_second_name:
            partner = self.env['res.partner'].search([('second_name', '=', self.partner_second_name.id)], limit=1)
            self.partner_id = partner if partner else False

