# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade

_tables_renames = [
    ("mail_channel", "discuss_channel"),
    ("mail_channel_member", "discuss_channel_member"),
    ("mail_channel_rtc_session", "discuss_channel_rtc_session"),
    ("hr_plan", "mail_activity_plan"),
    ("hr_plan_activity_type", "mail_activity_plan_template"),
]

_fields_renames = [
    (
        "mail.activity.plan.template",
        "mail_activity_plan_template",
        "responsible",
        "responsible_type",
    ),
]

_new_fields = [
    (
        "alias_domain_id",      # Field name
        "res.company",          # Model name
        False,                  # [Optional] Table name
        "many2one",             # Odoo Field type (in lower case)
        False,                  # [Optional] SQL type (if custom fields)
        "mail",                 # Module name
        False,                  # [Optional] Default value
    ),
]

def update_channel_xml_ids(env):
    openupgrade.logged_query(
        env.cr, 
        """
        UPDATE ir_model_data 
        SET model = REPLACE(model, 'mail.channel', 'discuss.channel') 
        WHERE module = 'mail' AND model ilike 'mail.channel%';
        """
    )

def update_mail_activity_plan_res_model(env):
    openupgrade.logged_query(
        env.cr,
        """
        ALTER TABLE mail_activity_plan ADD COLUMN res_model VARCHAR;
        UPDATE mail_activity_plan 
        SET res_model = 'hr.department' 
        WHERE id IN (
            SELECT res_id FROM ir_model_data WHERE module='hr' AND name IN ('offboarding_plan', 'onboarding_plan')
        );
        """
    )

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_tables(env.cr, _tables_renames)
    openupgrade.rename_fields(env, _fields_renames)
    openupgrade.add_fields(env, _new_fields)
    update_channel_xml_ids(env)
    update_mail_activity_plan_res_model(env)