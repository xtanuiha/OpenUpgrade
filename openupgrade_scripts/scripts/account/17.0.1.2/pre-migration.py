# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade

def update_account_report(env):
    openupgrade.logged_query(
        env.cr,
        """
        ALTER TABLE account_report
        ALTER COLUMN filter_account_type TYPE varchar 
        USING CASE WHEN filter_account_type THEN 'both' ELSE 'disabled' END;
        """
    )

@openupgrade.migrate()
def migrate(env, version):
    update_account_report(env)