# -*- coding: utf-8 -*-
# parte B
from odoo import models, fields, api


class lista_tareas(models.Model):
     _name = 'lista_tareas.lista_tareas'
     _description = 'lista_tareas.lista_tareas'

     avatar = fields.Image('Imagen tarea',max_width=50,max_heigth=50)
     tarea = fields.Char()
     fecha = fields.Date()
     prioridad = fields.Integer()
     urgente = fields.Boolean(compute="_value_urgente", store=True)
     realizada = fields.Boolean()
     descripcion = fields.Text()


     @api.depends('prioridad') 
     def _value_urgente(self):
     #Para cada registro
         for record in self:
            if record.prioridad>5:
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
