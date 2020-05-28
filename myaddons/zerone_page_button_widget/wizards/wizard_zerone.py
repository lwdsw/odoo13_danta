# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       ZERONE
# Date:         2020/2/5 上午10:16
# Description:

# -------------------------------------------------------------------------------

from odoo import fields, models


class WizardZerone(models.TransientModel):
    _name = "wizard.zerone"
    _description = "我的向导"

    message = fields.Text(string="提示", default="我的向导测试")

    def comfirm_test_wizard(self):
        record_selected = self._context.get("active_ids", [])
        print(record_selected)
        return {"type": "ir.actions.act_window_close"}