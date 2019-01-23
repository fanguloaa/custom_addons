# -*- coding: utf-8 -*-
from odoo import models, fields

class Library(models.Model):
    _name = 'mi_modulo.library'
    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char('Direccion', required=True)