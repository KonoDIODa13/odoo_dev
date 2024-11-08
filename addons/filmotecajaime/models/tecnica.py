# -*- coding: utf-8 -*-

from odoo import fields, models


class tecnica(models.Model):
    _name = "filmotecajaime.tecnica"
    _description = "filmotecajaime.tecnica"

    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el nombre"
    )
    description = fields.Text(string="Descripción")
    photo = fields.Image(string="Imagen")
    peliculas_id = fields.Many2many(
        comodel_name="filmotecajaime.pelicula",
        relation="tecnicas_peliculas",
        colum1="peliculas_ids",
        colum2="peliculas_ids",
    )
