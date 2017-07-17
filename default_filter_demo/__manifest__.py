# -*- coding: utf-8 -*-
{
    'name': "default_filter_demo",

    'summary': """
        A demo showing you how to add quick filters""",

    'description': """
        A demo showing you how to add quick filters
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/quotation_search.xml',
    ]
}
