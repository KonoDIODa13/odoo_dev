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


from odoo import http
from odoo.http import Response
import json


class pelicula_controller(http.Controller):

    @http.route("/api/peliculas", auth="public", method=["GET"], csrf=False)
    def get_peliculas(self, **kw):
        try:
            peliculas = http.request.env["filmotecajaime.pelicula"].sudo().search_read([], ["id", "name", "color"])
            res = json.dumps(peliculas, ensure_ascii=False).encode("utf-8")
            return Response(
                res, content_type="application/json;charset=utf-8", status=200
            )
        except Exception as e:
            return Response(
                json.dumps({"error": str(e)}),
                content_type="application/json;charset=utf-8",
                status=505,
            )
