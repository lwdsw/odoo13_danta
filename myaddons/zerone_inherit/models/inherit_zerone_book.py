# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       ZERONE
# Date:         2020/2/11 下午12:36
# Description:  

# -------------------------------------------------------------------------------

from odoo import api, fields, models


class ZeroneBook(models.Model):
    _inherit = "zerone.book"

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('zerone.book.sequence') or '/'
        res = super(ZeroneBook, self).create(vals)
        return res
