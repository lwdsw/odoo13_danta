from odoo import api, fields, models, _


class ZeroneBook(models.Model):
    _name = "zerone.book"
    _description = "Zerone Books"

    name = fields.Char(string="图书名称", required=True)
    code = fields.Char(string="图书编号", copy=False, help="管理编号，用于快速定位图书")
    isbn = fields.Char(string="ISBN", copy=False)
    author = fields.Char(string="作者")
    pages = fields.Integer(string="页数")
    publish_date = fields.Data(string="出版时间")
    publisher = fields.Char(string="出版社")
    price = fields.Float(string="定价", digits=(7, 2))
    description = fields.Text(string="内容简介", help="""向借阅者描述本书的内容""")
    binding_type = fields.Selection(
        [("common", "普通"), ("hardcover", "精装")],
        string="装帧类型", index=True, default='common'
    )
    e_link = fields.Html(string="电子版连接")
    borrowed = fields.Boolean(string="是否被借阅", default=False)
    date_last_borrowed = fields.Datetime("最后被借阅时间", index=True, readonly=True)
    category_ids = fields.One2many("zerone.book.category", "book_category_rel", "book_id", "category_id", string="类别")


class ZeroneBookCategory(models.Model):
    _name = "zerone.book.category"
    _description = "Zerone Book Categories"

    name = fields.Char("类别名称")
    category_ids = fields.Many2many("zerone.book.category", "book_category_rel", "book_id", "category_id", string="类别")

