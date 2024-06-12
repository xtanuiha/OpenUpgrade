# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


_deleted_xml_records = [
    "project.ir_cron_recurring_tasks",
    "project.mt_project_task_blocked",
    "project.mt_project_task_dependency_change",
    "project.mt_project_task_ready",
    "project.mt_task_blocked",
    "project.mt_task_dependency_change",
    "project.mt_task_progress",
    "project.mt_task_ready",
]


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
    openupgrade.delete_records_safely_by_xml_id(
        env,
        _deleted_xml_records,
    )
