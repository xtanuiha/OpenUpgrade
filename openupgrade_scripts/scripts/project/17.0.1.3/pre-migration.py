# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


def remove_columns(env):
    openupgrade.logged_query(
        env.cr,
        """
        DELETE FROM ir_model_data WHERE module = 'project' AND name = 'field_project_task__manager_id';
        DELETE FROM ir_model_fields WHERE model = 'project.task' AND name = 'manager_id';
        DELETE FROM ir_model_data WHERE module = 'project' AND name = 'field_project_task__kanban_state_label';
        DELETE FROM ir_model_fields WHERE model = 'project.task' AND name = 'kanban_state_label';
        """
    )


@openupgrade.migrate()
def migrate(env, version):
    remove_columns(env)
