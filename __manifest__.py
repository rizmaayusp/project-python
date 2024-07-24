# -*- coding: utf-8 -*-
{
    'name': "modulrizma",

    'summary': """
        modulrizma Software merupakan perusahaan top 1
        """,

    'description': """
        Perusahaan terbesar dan sudah melegenda 
    """,

    'author': "Rizma",
    'website': "http://www.vokasi.ub.ac.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/agama.xml',
        'views/mahasiswa.xml',
        'views/matakuliah.xml',
        'views/fakultas.xml',
        'views/prodi.xml',
        'views/ruang.xml',
        'views/hari.xml',
        'views/jadwal.xml',
        'views/semester.xml',
        'views/detailmk.xml',
        'views/angkatan.xml',
        'views/respartner.xml',
        'views/dosen.xml',
        'views/views.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
