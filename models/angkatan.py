from odoo import models, fields, api


class angkatan(models.Model):
    _name = 'modulrizma.angkatan'
    _description = 'menyimpan data angkatan'

    name = fields.Char(string ='Tahun Angkatan', required = True)