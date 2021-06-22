# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Gutachten(http.Controller):

    @http.route('/gutachten_webform1', type="http", auth="public", website=True)
    def gutachten_webform1(self, **kw):
       #gutachten = request.env['project.task'].sudo().search([])
       return http.request.render("PublicProjekt.search_gutachten", {})

class Gutachten1(http.Controller):

    @http.route('/gutachten_webform2', type="http", auth="public", website=True)
    def gutachten_webform2(self, **kw):
       project_rec = request.env['project.task'].sudo().search([])
       return http.request.render("PublicProjekt.search_gutachten2", {})


class GetTasksList(http.Controller):

    @http.route('/tasks/public', type="http", auth="public", website=True, csrf=False)
    def get_tasks_public(self, **kw):
       """Get Lis of tasks for public users."""
       number = kw.get('number', False)
       res = []
       if number:
           task_ids = request.env['project.task'].sudo().search([('name', '=', str(number))])
           for task in task_ids:
               vals= {'name': task.name,
                      'stage_name': task.stage_id.name if task.stage_id else ''}
               res.append(vals)

       return http.request.render("PublicProjekt.tasks_list", {'res': res})
