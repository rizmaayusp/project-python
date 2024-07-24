from odoo import models, fields, api

class dosen(models.Model):
    _name = 'modulrizma.dosen' # nama addons.nama tabel
    _description = 'menyimpan data dosen'

    name = fields.Char(string = 'Nama Dosen', required = True) # name sebagai field yang unique
    matakuliah_id = fields.Many2one(string="Nama Mata Kuliah",comodel_name="modulrizma.matakuliah",ondelete="restrict")
    fakultas_id = fields.Many2one(string="Nama Fakultas",comodel_name="modulrizma.fakultas",ondelete="restrict")

    _sql_constraints = [('name_uniq', 'unique(name)', 'Data sudah ada')]