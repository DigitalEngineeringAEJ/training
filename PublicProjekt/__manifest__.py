# -*- coding: utf-8 -*-
{
    'name' : 'PublicProject',
    'version' : '0.1',
    'summary': 'Project Access',
    'description': """
Ermöglicht den Zugang zu seinem Projekt als Public User
    """,
    'category': 'Projekt',
    'website': 'https://www.deaejodoo.com/',
    'depends' : ['base', 'website', 'project'],
    'data': [
        'views/website_form.xml',
        'views/website_form1.xml'
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
