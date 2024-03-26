# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


def upadte_ir_property_type(env):
    openupgrade.logged_query(
        env.cr,
        "UPDATE ir_property SET type = 'text' WHERE type = 'html';"
    )

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env, "base", "17.0.1.3/noupdate_changes.xml")
    upadte_ir_property_type(env)
