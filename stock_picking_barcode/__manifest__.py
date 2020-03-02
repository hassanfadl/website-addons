# -*- coding: utf-8 -*-
{
    "name": """Barcode scanner for Stock""",
    "summary": """The module allows you to process Pickings by barcode scanner via special page /barcode/web (the same as it was in odoo 8.0)""",
    "category": "Warehouse",
    "images": [],
    "vesion": "10.0.1.0.3",
    "author": "IT-Projects LLC, Pavel Romanchenko",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info",
    "license": "Other OSI approved licence",  # MIT
    "price": 89.00,
    "currency": "EUR",
    "depends": ["stock", "web_editor", "website"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/stock.xml", "views/stock_view.xml", "views/stock_dashboard.xml"],
    "qweb": ["static/src/xml/picking.xml"],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
}
