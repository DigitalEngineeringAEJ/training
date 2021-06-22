from odoo import api, fields, models

class PublicProject(models.Model):
    _inherit = 'project.project'

    task_user =fields.Many2one('project.task', string='Gutachten')