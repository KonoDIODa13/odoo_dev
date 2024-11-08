# -*- coding: utf-8 -*-

from odoo import models, fields


class genero(models.Model):
    _name = "filmotecajaime.genero"
    _description = "filmotecajaime.genero"

    name = fields.Char(
        string="Nombre",
        readonly=False,
        required=True,
        help="Introduzca el nombre del genero",
    )
    description = fields.Text(string="Descripcion")
    peliculas_id = fields.One2many(
        string="Películas", comodel_name="filmotecajaime.pelicula", inverse_name="genero_id"
    )
