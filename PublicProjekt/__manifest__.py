# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'PubllicProject',
    'version' : '0.1',
    'summary': 'Project Access',
    'description': """
Ermöglicht den Zugang zu seinem Projekt als Public User
    """,
    'category': 'Projekt',
    'website': 'https://www.deaejodoo.com/',
    'depends' : ['base'],
    'data': [
        'views/website_form.xml'
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
