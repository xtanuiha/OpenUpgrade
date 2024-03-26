# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


def update_hr_plan_to_mail_activity_plan(env):
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE ir_model_data SET model = 'mail.activity.plan' WHERE module = 'hr' AND model = 'hr.plan';
        UPDATE ir_model_data SET model = 'mail.activity.plan.template' WHERE module = 'hr' AND model = 'hr.plan.activity.type';
        """
    )


def remove_columns(env):
    openupgrade.logged_query(
        env.cr,
        """
        DELETE FROM ir_model_data WHERE module = 'hr' AND name = 'field_hr_employee__phone';
        DELETE FROM ir_model_fields WHERE model = 'hr.employee' AND name = 'phone';
        """
    )


@openupgrade.migrate()
def migrate(env, version):
    update_hr_plan_to_mail_activity_plan(env)
    remove_columns(env)
