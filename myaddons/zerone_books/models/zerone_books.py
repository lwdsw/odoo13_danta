from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _


class ZeroneBook(models.Model):
    _name = "zerone.book"
    _description = "Zerone Books"

    name = fields.Char(string="图书名称")
    code = fields.Char(string="图书编号")



