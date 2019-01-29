# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Library Management
        """,

    'author': "OEC",
    'website': "https://www.odooerpcloud.com",

    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library_book_category_view.xml',
        # 'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}

