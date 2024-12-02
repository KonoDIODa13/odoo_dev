# -*- coding: utf-8 -*-
# from odoo import http


# class Managejaime(http.Controller):
#     @http.route('/managejaime/managejaime', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managejaime/managejaime/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managejaime.listing', {
#             'root': '/managejaime/managejaime',
#             'objects': http.request.env['managejaime.managejaime'].search([]),
#         })

#     @http.route('/managejaime/managejaime/objects/<model("managejaime.managejaime"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managejaime.object', {
#             'object': obj
#         })
