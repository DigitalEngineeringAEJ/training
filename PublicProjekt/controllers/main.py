# -*- coding: utf-8 -*-
import odoo
from odoo import models, fields
from odoo import http
from odoo.http import request


class Gutachten(http.Controller):

    @http.route('/search_gutachten', type="http", auth="public", website=True)
    def search_gutachten(self, **kw):
        return http.request.render('PublicProject.search_gutachten', {})





