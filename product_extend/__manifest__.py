# -*- coding: utf-8 -*-
{
    'name': "Product Extend (Ejemplo Herencia)",

    'summary': """
        Ejemplo Herencia en el modulo product
        Agregar un campo seleccionable Tipologia
        """,

    'author': "OEC",
    'website': "https://www.odooerpcloud.com",

    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/product_view.xml',
    ],
    'installable': True,
    'application': True,
}

