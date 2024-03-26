
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env.ref('auth_signup.reset_password_email').unlink()
