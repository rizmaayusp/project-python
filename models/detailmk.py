from odoo import models, fields, api

class detailmk(models.Model):
    _name = 'modulrizma.detailmk' # nama addons.nama tabel
    _description = 'menyimpan data detail Mata Kuliah'

    mahasiswa_id = fields.Many2one(string="Nama Mahasiswa",comodel_name="modulrizma.mahasiswa",ondelete="restrict")
    matakuliah_id = fields.Many2one(string="Nama Mata Kuliah",comodel_name="modulrizma.matakuliah",ondelete="restrict")
    semester_id = fields.Many2one(string="Semester",comodel_name="modulrizma.semester",ondelete="restrict")
    nilai_uts = fields.Float(string = 'Nilai UTS', required = True) # name sebagai field yang unique
    nilai_uas = fields.Float(string = 'Nilai UAS', required = True) # name sebagai field 
    tugas = fields.Float(string = 'Nilai Tugas', required = True) # name sebagai field yang unique
    quiz = fields.Float(string = 'Nilai Quiz', required = True) # name sebagai field 

    total = fields.Float(compute="_compute_total") 

    @api.depends("nilai_uts", "nilai_uas", "tugas", "quiz",)
    def _compute_total(self):
        for record in self:
            record.total = (0.15 * record.nilai_uts) + (0.15 * record.nilai_uas) + (0.5 * record.tugas) + (0.2 * record.quiz)
