# -*- coding: utf-8 -*-

{
    "name": "Account Credit Transfer",
    "version": "1.0.3",
    "author": "XCG Consulting",
    "website": "http://www.openerp-experts.com",
    "category": 'Accounting',
    "description": """Account Voucher Credit Transfer Payment.
    You need to set up some things before using it.
    A credit transfer config link a bank with a parser
    A credit transfer parser link a parser with a template that you can upload
    """,

    "depends": [
        'base',
        'account_streamline',
        'analytic_structure',
    ],

    "data": [
        "security/ir.model.access.csv",
        "views/config.xml",
        "views/parser.xml",
        "views/res.bank.xml",
    ],

    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
    'external_dependencies': {
        'python': ['genshi']
    }
}
