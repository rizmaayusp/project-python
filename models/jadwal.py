from odoo import models, fields, api

class jadwal(models.Model):
    _name = 'modulrizma.jadwal' # nama addons.nama tabel
    _description = 'menyimpan data jadwal'

    kodejadwal = fields.Char(string = 'Kode jadwal', required = True) # name sebagai field yang unique
    matakuliah_id = fields.Many2one(string="Nama matakuliah",comodel_name="modulrizma.matakuliah",ondelete="restrict")
    hari_id = fields.Many2one(string="Hari",comodel_name="modulrizma.hari",ondelete="restrict")
    jam_mulai = fields.Float(string = 'Jam Mulai', required = True) # name sebagai field 
    jam_selesai = fields.Float(string = 'Jam Selesai', required = True) # name sebagai field 
    prodi_id = fields.Many2one(string="Nama Prodi",comodel_name="modulrizma.prodi",ondelete="restrict")    