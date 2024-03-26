# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


def remove_columns(env):
    openupgrade.logged_query(
        env.cr,
        """
        DELETE FROM ir_model_data WHERE module = 'hr_recruitment' AND name = 'field_hr_employee__hr_responsible_id';
        DELETE FROM ir_model_fields WHERE model = 'hr.job' AND name = 'hr_responsible_id';
        """
    )


@openupgrade.migrate()
def migrate(env, version):
    remove_columns(env)
