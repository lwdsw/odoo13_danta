
from odoo import api, fields, models, _


class ZeroneTags(models.Model):
    _name = "zerone.tags"
    _description = "Zerone Tags"

    name = fields.Char("标签名称", size=10)
