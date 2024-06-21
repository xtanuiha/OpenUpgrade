# Copyright 2023 Odoo Community Association (OCA)
# Copyright 2023 Shanghai Yumtown <info@yumtown.com.cn>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


def _update_stock_move_quantity(env):
    openupgrade.logged_query(
        env,
        "UPDATE stock_move SET quantity = quantity_done WHERE quantity_done != 0;"
    )


def _update_stock_move_scrap(env):
    sql = 'SELECT id,move_id FROM stock_scrap WHERE move_id IS NOT NULL;'
    env.cr.execute(sql)
    scrap_dict = env.cr.dictfetchall()
    scrap_dict = dict([(item['id'], item['move_id']) for item in scrap_dict])
    for scrap in env['stock.scrap'].search([('id', 'in', list(scrap_dict.keys()))]):
        scrap.write({'move_ids': [(4, scrap_dict[scrap.id])]})


def _update_stock_move_line_quantity(env):
    openupgrade.logged_query(
        env,
        "UPDATE stock_move_line SET quantity = qty_done WHERE qty_done != 0;"
    )


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env, "stock", "17.0.1.1/noupdate_changes.xml")
    _update_stock_move_quantity(env)
    _update_stock_move_scrap(env)
    _update_stock_move_line_quantity(env)
