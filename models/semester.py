from odoo import models, fields, api

class semester(models.Model):
    _name = 'modulrizma.semester' # nama addons.nama tabel
    _description = 'menyimpan data semester'

    name = fields.Char(string = 'Semester', required = True) # name sebagai field yang unique
    _sql_constraints = [('name_uniq', 'unique(name)', 'Data sudah ada')]