
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env.ref("sale_management.res_config_settings_view_form_inherit_sale_management").unlink()
