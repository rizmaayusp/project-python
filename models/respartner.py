from odoo import models, fields, api

class Respartner(models.Model):
    _inherit = "res.users"

    jadwal_ids = fields.Many2many("modulrizma.jadwal", string="Data Jadwal")