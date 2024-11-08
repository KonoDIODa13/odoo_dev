# -*- coding: utf-8 -*-

import datetime
from odoo import fields, models


class pelicula(models.Model):
    _name = "filmotecajaime.pelicula"
    _description = "filmotecajaime.pelicula"

    code = fields.Char(string="Código", compute="_get_code")
    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el nombre"
    )
    description = fields.Text(string="Descripción")
    film_date = fields.Date(string="Fecha de la Peli")
    start_date = fields.Datetime(string="Fecha de Salida")
    end_date = fields.Datetime(string="Fecha Final")
    is_spanish = fields.Boolean(string="Es española")
    image = fields.Image(string="Cartel")
    language = fields.Selection(
        [("es", "español"), ("en", "english"), ("ja", "japanese")],
        string="Idioma",
        default="en",
    )
    opinion = fields.Selection(
        [("0", "mala"), ("1", "regular"), ("2", "buena")], string="Opinion", default="1"
    )
    color = fields.Boolean(string="Esta a color")
    genero_id = fields.Many2one(
        "filmotecajaime.genero", string="Género", required=True, ondelete="cascade"
    )
    tecnicas_id = fields.Many2many(
        comodel_name="filmotecajaime.tecnica",
        relation="tecnicas_peliculas",
        colum1="peliculas_ids",
        colum2="peliculas_ids",
    )

    # @api.one Para recibir un único objeto
    def _get_code(self):
        for pelicula in self:
            if len(pelicula.genero_id) == 0:
                pelicula.code = "FILM_" + str(pelicula.id)
            else:
                pelicula.code = (
                    str(pelicula.genero_id.name).upper() + "_" + str(pelicula.id)
                )

    def toggle_color(self):
        self.color = not self.color

    def f_create(self):
        pelicula = {
            "name": "Proeba ORM",
            "color": True,
            "genero_id": 1,
            "start_date": str(datetime.date(2022, 8, 8)),
        }
        print(pelicula)
        self.env["filmotecajaime.pelicula"].create(pelicula)

    def f_update(self):
        self.write({"name": ""})
        self.write({"name": "pelicula modificada"}) 

    def f_delete(self):
        self.unlink()
