# -*- coding: utf-8 -*-
# from odoo import http


# class Mundotec(http.Controller):
#     @http.route('/mundotec/mundotec', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mundotec/mundotec/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mundotec.listing', {
#             'root': '/mundotec/mundotec',
#             'objects': http.request.env['mundotec.mundotec'].search([]),
#         })

#     @http.route('/mundotec/mundotec/objects/<model("mundotec.mundotec"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mundotec.object', {
#             'object': obj
#         })
