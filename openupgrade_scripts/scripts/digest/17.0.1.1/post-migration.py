# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env, "digest", "17.0.1.1/noupdate_changes.xml")
