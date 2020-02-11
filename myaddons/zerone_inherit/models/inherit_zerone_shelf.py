# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       ZERONE
# Date:         2020/2/11 下午12:36
# Description:  

# -------------------------------------------------------------------------------

from odoo import api, fields, models, _


class ZeroneShelf(models.Model):
    _inherit = "zerone.shelf"

    description = fields.Text(string="书架说明")

    name = fields.Char(string="名称", size=32)

    def say_hello(self):
        print("hello")

    def write(self, vals):
        res = super(ZeroneShelf, self).write(vals)
        print("我是重写方法", vals)
        return res
