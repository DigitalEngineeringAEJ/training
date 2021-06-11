# -*- coding: utf-8 -*-

{
    'name' : 'FSMOD',
    'version' : '0.1',
    'summary': 'FSMOD',
    'description': """
    FSMOD is for testing
    """,
    'category': 'test',
    'website': 'https://www.eaj.odoo.com',
    'depends' : ['base'],
    'data': ['security/ir.model.access.csv'
        'views/fs_views.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
