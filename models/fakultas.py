from odoo import models, fields, api

class fakultas(models.Model):
    _name = 'modulrizma.fakultas' # nama addons.nama tabel
    _description = 'menyimpan data fakultas'

    name = fields.Char(string = 'Nama Fakultas', required = True) # name sebagai field yang unique
    _sql_constraints = [('name_uniq', 'unique(name)', 'Data sudah ada')]