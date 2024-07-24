from odoo import models, fields, api

class hari(models.Model):
    _name = 'modulrizma.hari' # nama addons.nama tabel
    _description = 'menyimpan data hari'

    name = fields.Char(string = 'Nama hari', required = True) # name sebagai field yang unique
    _sql_constraints = [('name_uniq', 'unique(name)', 'Data sudah ada')]