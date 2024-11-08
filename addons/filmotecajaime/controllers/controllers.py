# -*- coding: utf-8 -*-
# from odoo import http


# class Filmotecajaime(http.Controller):
#     @http.route('/filmotecajaime/filmotecajaime', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmotecajaime/filmotecajaime/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmotecajaime.listing', {
#             'root': '/filmotecajaime/filmotecajaime',
#             'objects': http.request.env['filmotecajaime.filmotecajaime'].search([]),
#         })

#     @http.route('/filmotecajaime/filmotecajaime/objects/<model("filmotecajaime.filmotecajaime"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmotecajaime.object', {
#             'object': obj
#         })
