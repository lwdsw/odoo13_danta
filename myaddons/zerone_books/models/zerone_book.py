from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ZeroneBook(models.Model):
    _name = "zerone.book"
    _inherit = ['image.mixin']
    _description = "Zerone Books"

    image_1920 = fields.Image(string="图书样例")

    name = fields.Char(string="图书名称", required=True)
    code = fields.Char(string="图书编号", copy=False, help="管理编号，用于快速定位图书")
    isbn = fields.Char(string="ISBN", copy=False)
    author = fields.Char(string="作者")
    pages = fields.Integer(string="页数")
    publish_date = fields.Date(string="出版时间")
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

    shelf_id = fields.Many2one('zerone.shelf', string='所在书架')
    tags_ids = fields.Many2many("zerone.tags", string="标签")

    @api.depends('isbn', 'name')
    def name_get(self):
        result = []
        for book in self:
            result.append((book.id, '%s(%s)' % (book.name, book.isbn)))
        return result

    @api.constrains('code')
    def _check_description(self):
        if self.search_count([('code', '=', self.code)]) > 1:
            raise ValidationError("图书编号必须是唯一的！")

    def action_text(self):
        print("表单视图中的按钮")

    def button_call_function1(self):
        self.borrowed = False

    def button_call_function2(self):
        self.borrowed = True
