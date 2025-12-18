from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'sale.order'

    sale_second_name = fields.Many2one(
        'second.name',
        string="Second Name",
        compute='_compute_sale_second_name',
        store=True,
        index=True,
        readonly=False
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        compute='_compute_sale_second_name',
        store=True,
        readonly=False
    )

    @api.depends('partner_id')
    def _compute_sale_second_name(self):
        for record in self:
            record.sale_second_name = record.partner_id.second_name if record.partner_id else ''

    @api.onchange('sale_second_name')
    def _onchange_sale_second_name(self):
        if self.sale_second_name:
            partner = self.env['res.partner'].search([('second_name', '=', self.sale_second_name.id)], limit=1)
            self.partner_id = partner if partner else False
