# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       ZERONE
# Date:         2019/12/27 下午8:20
# Description:  

# -------------------------------------------------------------------------------

from odoo import api, fields, models, _


class ZeroneShelf(models.Model):
    _name = "zerone.shelf"
    _description = "Zerone Shelf"

    name = fields.Char("书架名称")
    capacity = fields.Integer("书架容量")
    capacity_rate = fields.Float(string="图书放置比", compute="_compute_rate")

    book_ids = fields.One2many('zerone.book', 'shelf_id', string="图书")

    @api.depends('capacity', 'book_ids')
    def _compute_rate(self):
        for record in self:
            if not record.capacity:
                record.capacity_rate = 0.0
            else:
                record.capacity_rate = 100.0 * len(record.book_ids) / record.capacity
