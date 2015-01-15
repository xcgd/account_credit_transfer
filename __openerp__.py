# -*- coding: utf-8 -*-
##############################################################################
#
#    Account Credit Transfer, for OpenERP
#    Copyright (C) 2013 XCG Consulting (http://odoo.consulting)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Account Credit Transfer",
    "version": "1.1",
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
