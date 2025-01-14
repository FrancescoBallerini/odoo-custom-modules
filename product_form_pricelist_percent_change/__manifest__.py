#  Copyright 2023 Francesco Ballerini
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Form Pricelist Percent Change",
    "version": "14.0.0.0.1",
    "category": "Product",
    "summary": """
        Enable, on pricelists views, percentage change computation
        and price simulation (only for rules applied at product level).
    """,
    "author": "Francesco Ballerini",
    "support": "francescobl.lavoro@gmail.com",
    "depends": ["product_form_pricelist", "base_view_inheritance_extension"],
    "data": [
        "views/product_template_view.xml",
        "views/product_pricelist_views.xml",
    ],
    "post_init_hook": "_post_init_hook",
    "application": False,
    "installable": True,
    "license": "AGPL-3",
}
