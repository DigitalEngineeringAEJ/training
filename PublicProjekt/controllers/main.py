# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Gutachten(http.Controller):

    @http.route('/gutachten_webform1', type="http", auth="public", website=True)
    def gutachten_webform1(self, **kw):
       #gutachten = request.env['project.task'].sudo().search([])
        return http.request.render("PublicProjekt.search_gutachten", {})

class Gutachten1(http.Controller):

    @http.route('/gutachten_webform1', type="http", auth="public", website=True)
    def gutachten_webform1(self, **kw):
       #gutachten = request.env['project.task'].sudo().search([])
        return http.request.render("PublicProjekt.search_gutachten1", {})



