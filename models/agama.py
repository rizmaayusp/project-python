from odoo import models, fields, api

class agama(models.Model):
    _name = 'modulrizma.agama' # nama addons.nama tabel
    _description = 'menyimpan data agama'

    name = fields.Char(string = 'Nama Agama', required = True) # name sebagai field yang unique
    _sql_constraints = [('name_uniq', 'unique(name)', 'Data sudah ada')]