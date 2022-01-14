# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lista_tareas(models.Model):
     _name = 'lista_tareas.lista_tareas'
     _description = 'lista_tareas.lista_tareas'
     tarea = fields.Char()
     prioridad = fields.Integer()
     urgente = fields.Boolean(compute="_value_urgente", store=True)
     realizada = fields.Boolean()
     fecha = fields.Date()
     def _value_urgente(self):
     #Para cada registro
      for record in self:
         if record.prioridad>10:
            record.urgente=True
         else:
            record.urgente = False
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
