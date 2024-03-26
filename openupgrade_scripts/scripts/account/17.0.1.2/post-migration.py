# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade

def update_company(env):
    openupgrade.logged_query(
        env.cr,
        "UPDATE res_company SET invoice_is_download = invoice_is_print;"
    )

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env, "account", "17.0.1.2/noupdate_changes.xml")
    update_company(env)