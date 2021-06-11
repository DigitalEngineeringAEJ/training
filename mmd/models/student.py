
from odoo import fields, models


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student"

    name = fields.Char(string='Name')
