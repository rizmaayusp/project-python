# -*- coding: utf-8 -*-
# from odoo import http


# class Modulrizma(http.Controller):
#     @http.route('/modulrizma/modulrizma', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulrizma/modulrizma/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulrizma.listing', {
#             'root': '/modulrizma/modulrizma',
#             'objects': http.request.env['modulrizma.modulrizma'].search([]),
#         })

#     @http.route('/modulrizma/modulrizma/objects/<model("modulrizma.modulrizma"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulrizma.object', {
#             'object': obj
#         })
