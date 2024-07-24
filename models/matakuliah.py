from odoo import models, fields, api

class Matakuliah(models.Model):
    _name = 'modulrizma.matakuliah' 
    _description = 'menyimpan data mata kuliah'

    KodeMK = fields.Char(string = 'Kode Mata Kuliah', required = True) 
    name = fields.Char(string = 'Nama Mata Kuliah', required = True) 
    SKS = fields.Integer(string = 'Jumlah SKS Mata Kuliah', required = True) 
    _sql_constraints = [('KodeMK_uniq', 'unique(KodeMK)', 'Data sudah ada')]

    rps = fields.Binary(string='Rencana Pembelajaran Semester', attachment=True, required=True )