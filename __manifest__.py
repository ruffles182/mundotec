# -*- coding: utf-8 -*-
{
    'name': "mundotec",

    'summary': """
        Modulo personalizado para la empresa Mundodelatecnologia""",

    'description': """
        cambios al módulo de reparaciones con campos personalizados.
    """,

    'author': "Rfflz",
    'website': "https://github.com/ruffles182",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'repair'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
