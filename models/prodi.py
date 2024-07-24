from odoo import models, fields, api

class prodi(models.Model):
    _name = 'modulrizma.prodi' # nama addons.nama tabel
    _description = 'menyimpan data prodi'

    name = fields.Char(string = 'Nama Program Studi', required = True) # name sebagai field yang unique    
    _sql_constraints = [('name_uniq', 'unique(name)', 'Data sudah ada')]
    fakultas_id = fields.Many2one(string="Nama Fakultas",comodel_name="modulrizma.fakultas",ondelete="restrict")