# -*- coding: utf-8 -*-
# from odoo import http


# class Abfrage(http.Controller):
#     @http.route('/abfrage/abfrage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abfrage/abfrage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abfrage.listing', {
#             'root': '/abfrage/abfrage',
#             'objects': http.request.env['abfrage.abfrage'].search([]),
#         })

#     @http.route('/abfrage/abfrage/objects/<model("abfrage.abfrage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abfrage.object', {
#             'object': obj
#         })
