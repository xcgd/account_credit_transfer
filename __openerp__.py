# -*- coding: utf-8 -*-

{
    "name": "Account Credit Transfer",
    "version": "0.1",
    "author": "XCG Consulting",
    "website": "http://www.openerp-experts.com",
    "category": 'Accounting',
    "description": """Account Voucher Credit Transfer Payment.
    """,

    "depends": [
        'base',
        'account_voucher',
    ],

    "data": [
        "views/config.xml",
        "views/parser.xml",
    ],

    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
    'external_dependencies': {
        'python': ['genshi']
    }
}
