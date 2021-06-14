# -*- coding: utf-8 -*-
import odoo
from odoo import fields, api, models
from odoo import http
from odoo.http import request
from odoo.addons.http_routing.controllers.main import WebClient, Routing

class Gutachten(http.Controller):

    @http.route('/search_gutachten', type="http", auth="public", website=True)
    def search_gutachten(self,**kw):
        return http.request.render('',{})





