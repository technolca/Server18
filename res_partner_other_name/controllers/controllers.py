# -*- coding: utf-8 -*-
# from odoo import http


# class ResPartnerOtherName(http.Controller):
#     @http.route('/res_partner_other_name/res_partner_other_name', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/res_partner_other_name/res_partner_other_name/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('res_partner_other_name.listing', {
#             'root': '/res_partner_other_name/res_partner_other_name',
#             'objects': http.request.env['res_partner_other_name.res_partner_other_name'].search([]),
#         })

#     @http.route('/res_partner_other_name/res_partner_other_name/objects/<model("res_partner_other_name.res_partner_other_name"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('res_partner_other_name.object', {
#             'object': obj
#         })

