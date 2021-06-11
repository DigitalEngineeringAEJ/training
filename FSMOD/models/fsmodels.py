# -*- coding: utf-8 -*-
from odoo import fields, models


class FSonModel(models.Model):
    _name = "fs.model"
    _description = "fs"

    name = fields.Char(string='Name')
    beschreibung = fields.Text(string='Beschreibung')

