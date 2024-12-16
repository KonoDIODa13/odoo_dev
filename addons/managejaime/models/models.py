# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class task(models.Model):
    _name = "managejaime.task"
    _description = "managejaime.task"

    code = fields.Char(string="Código", compute="_get_code")
    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el nombre"
    )
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="fecha Inicio")
    end_date = fields.Datetime(string="fecha Fin")
    is_paused = fields.Boolean(string="Pausado")
    sprint_id = fields.Many2one(
        "managejaime.sprint",
        string="Sprint",
        # required=True,
        ondelete="cascade",
        compute="_get_sprint",
        store=True,
    )
    history_id = fields.Many2one(
        "managejaime.history", string="Historias", required=True, ondelete="cascade"
    )
    """project_id = fields.Many2one(
        "managejaime.project", related="history.project_id", readonly=True
    )"""

    technologys_id = fields.Many2many(
        comodel_name="managejaime.technology",
        relation="technology_task",
        colum1="technologys_ids",
        colum2="tasks_ids",
    )

    def _get_code(self):
        for task in self:
            task.code = "TASK_" + str(task.id)

    @api.depends("code")
    def _get_sprint(self):
        for task in self:
            sprints = self.env["managejaime.sprint"].search(
                [("project_id.id", "=", task.history_id.project_id.id)]
            )
            found = False
            for sprint in sprints:
                if (
                    isinstance(sprint.end_date, datetime.datetime)
                    and sprint.end_date > datetime.datetime.now()
                ):
                    task.sprint_id = sprint.id
                    found = True
            if not found:
                task.sprint_id = False


class sprint(models.Model):
    _name = "managejaime.sprint"
    _description = "managejaime.sprint"

    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el nombre"
    )
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha Inicio")
    duration = fields.Integer(string="Duración")
    end_date = fields.Datetime(string="fecha Fin", compute="_get_end_date", store=True)
    project_id = fields.Many2one(
        "managejaime.project", string="Proyectos", required=True, ondelete="cascade"
    )
    tasks_id = fields.One2many(
        string="Tasks", comodel_name="managejaime.task", inverse_name="sprint_id"
    )

    @api.depends("start_date", "duration")
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(
                    days=sprint.duration
                )
            else:
                sprint.end_date = sprint.start_date


class project(models.Model):
    _name = "managejaime.project"
    _description = "managejaime.project"

    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el nombre"
    )
    description = fields.Text(string="Descripción")
    sprints_id = fields.One2many(
        string="Sprints", comodel_name="managejaime.sprint", inverse_name="project_id"
    )
    historys_id = fields.One2many(
        string="Historias",
        comodel_name="managejaime.history",
        inverse_name="project_id",
    )


class history(models.Model):
    _name = "managejaime.history"
    _description = "managejaime.history"

    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el nombre"
    )
    description = fields.Text(string="Descripción")
    project_id = fields.Many2one(
        "managejaime.project", string="Proyectos", required=True, ondelete="cascade"
    )
    tasks_id = fields.One2many(
        string="Tareas", comodel_name="managejaime.task", inverse_name="history_id"
    )

    used_technologies = fields.Many2many(
        "manage.technology", compute="_get_used_technologies"
    )

    def _get_used_technologies(self):
        for history in self:
            technologies = None
            for task in history.tasks_id:
                if not technologies:
                    technologies = task.technologys_id
                else:
                    technologies = technologies + task.technologys_id
        history.used_technologies = technologies


class technology(models.Model):
    _name = "managejaime.technology"
    _description = "managejaime.technology"

    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el nombre"
    )
    description = fields.Text(string="Descripción")
    photo = fields.Image(string="Imagen")
    tasks_id = fields.Many2many(
        comodel_name="managejaime.task",
        relation="technology_task",
        colum1="technologys_ids",
        colum2="tasks_ids",
    )

"""class developer(models.Model):
    _name = "res.partner"
    _inherits = "res.partner"

    technologies = fields.Many2many(
        "manage.technology",
        relation="developer_technologies",
        column1="developer_id",
        column2="technologies_id",
    )"""
