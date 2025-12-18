# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrderanalyticAccount(models.Model):
    _inherit = "sale.order"

    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        ondelete='set null',
        copy=False,
    )

    def _create_analytic_account(self):
        """Create an analytic account and link it to the sale order."""
        # Fetch a default analytic plan (adjust domain as needed)
        plan = self.env['account.analytic.plan'].search([], limit=1)
        if not plan:
            raise UserError(_("No Analytic Plan found. Please create one first."))

        analytic_account = self.env['account.analytic.account'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,
            'plan_id': plan.id,  # Set the required plan_id
        })
        self.analytic_account_id = analytic_account.id

    def _action_confirm(self):
        """ On SO confirmation, analytic account will be created automatically. """
        result = super(SaleOrderanalyticAccount, self)._action_confirm()
        # if the SO not already linked to analytic account, create a new analytic account and set to so analytic account.
        for order in self:
            if not order.analytic_account_id:
                order._create_analytic_account()
        return result

    @api.depends('is_subscription', 'state', 'start_date', 'subscription_state')
    def _compute_next_invoice_date(self):
        for so in self:
            if not so.is_subscription and so.subscription_state != '7_upsell':
                so.next_invoice_date = False
            elif not so.next_invoice_date and so.state == 'draft':
                so.next_invoice_date = so.start_date or fields.Date.today()


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_post(self):
        res = super().action_post()
        
        # الحل الأول: استخدام try-except لتجنب الخطأ
        for rec in self:
            try:
                self.env['mail.message'].sudo().create({
                    'model': rec._name,
                    'res_id': rec.id,
                    'message_type': 'comment',
                    'subtype_id': self.env.ref('mail.mt_note').id,
                    'body': _("Payment has been created and posted."),
                })
            except Exception as e:
                # تسجيل الخطأ في اللوج بدلاً من إيقاف العملية
                import logging
                _logger = logging.getLogger(__name__)
                _logger.warning(f"Could not create mail message for payment {rec.id}: {str(e)}")
        
        return res

    # الحل البديل الثاني: استخدام message_post بدلاً من إنشاء mail.message مباشرة
    def action_post_alternative(self):
        res = super().action_post()
        for rec in self:
            try:
                rec.message_post(
                    body=_("Payment has been created and posted."),
                    subtype_xmlid='mail.mt_note'
                )
            except Exception as e:
                import logging
                _logger = logging.getLogger(__name__)
                _logger.warning(f"Could not post message for payment {rec.id}: {str(e)}")
        return res

    # الحل الثالث: التحقق من الصلاحيات أولاً
    def action_post_with_permission_check(self):
        res = super().action_post()
        for rec in self:
            # التحقق من وجود الصلاحيات أولاً
            if self.env['mail.message'].check_access_rights('create', raise_exception=False):
                try:
                    self.env['mail.message'].sudo().create({
                        'model': rec._name,
                        'res_id': rec.id,
                        'message_type': 'comment',
                        'subtype_id': self.env.ref('mail.mt_note').id,
                        'body': _("Payment has been created and posted."),
                    })
                except Exception:
                    pass  # تجاهل الخطأ
        return res