from odoo import models, fields, api

class Mahasiswa(models.Model):
    _name = 'modulrizma.mahasiswa' 
    _description = 'menyimpan data mahasiswa'

    name = fields.Char(string = 'Nama Mahasiswa', required = True) 
    nim = fields.Char(string = 'NIM Mahasiswa', required = True) 
    alamat = fields.Text(string = 'Alamat Mahasiswa', required = True)
    birth = fields.Date(string = 'Tanggal Lahir', required = True) 
    telp = fields.Char(string = 'Telepon Mahasiswa', required = True)
    ayah = fields.Char(string = 'Ayah', required = True)
    ibu = fields.Char(string = 'Ibu', required = True)
    pekerjaanAyah = fields.Char(string = 'Pekerjaan Ayah', required = True)
    pekerjaanIbu = fields.Char(string = 'Pekerjaan Ibu', required = True)
    message_ids = fields.Char(string = 'Pesan Email', required = True)
    agama_id = fields.Many2one(string="Nama Agama",comodel_name="modulrizma.agama",ondelete="restrict")
    angkatan_id = fields.Many2one(string="Tahun Angkatan",comodel_name="modulrizma.angkatan",ondelete="restrict")
    _sql_constraints = [('nim_uniq', 'unique(nim)', 'Data NIM sudah ada')]
    image = fields.Binary(string = 'Image', attachment = True, required = True)