# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade

def update_mail_tracking_value(env):
    openupgrade.logged_query(
        env.cr, 
        """
        UPDATE mail_tracking_value SET field_id = field WHERE field IS NOT NULL;
        UPDATE mail_tracking_value SET old_value_float = old_value_monetary WHERE old_value_monetary IS NOT NULL;
        UPDATE mail_tracking_value SET new_value_float = new_value_monetary WHERE new_value_monetary IS NOT NULL;
        """
    )


def fix_mail_alias_model(env):
    channel_model_id = env.ref('mail.model_discuss_channel')
    env['mail.alias'].search([('alias_model_id.model', '=', 'mail.channel')]).write({'alias_model_id': channel_model_id.id})
    env['mail.alias'].search([('alias_parent_model_id.model', '=', 'mail.channel')]).write({'alias_parent_model_id': channel_model_id.id})


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env, "mail", "17.0.1.15/noupdate_changes.xml")
    update_mail_tracking_value(env)
    openupgrade.m2o_to_x2m(env.cr, env["mail.template"], "mail_template", "report_template_ids", "report_template")
    fix_mail_alias_model(env)
