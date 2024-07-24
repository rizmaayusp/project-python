from odoo import models, fields, api

class ruang(models.Model):
    _name = 'modulrizma.ruang' # nama addons.nama tabel
    _description = 'menyimpan data ruang'

    name = fields.Char(string = 'Nama ruang', required = True) # name sebagai field yang unique
    _sql_constraints = [('name_uniq', 'unique(name)', 'Data sudah ada')]