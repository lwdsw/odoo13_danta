from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ZeroneBook(models.Model):
    _name = "zerone.book"
    _inherit = ['image.mixin']
    _description = "Zerone Books"

    image_1920 = fields.Image(string="图书样例")

    # image_1920 = fields.Image("图书样例", compute='_compute_image', compute_sudo=True)
    # image_1024 = fields.Image("Image 1024", compute='_compute_image', compute_sudo=True)
    # image_512 = fields.Image("Image 512", compute='_compute_image', compute_sudo=True)
    # image_256 = fields.Image("Image 256", compute='_compute_image', compute_sudo=True)
    # image_128 = fields.Image("Image 128", compute='_compute_image', compute_sudo=True)
    #
    # def _compute_image(self):
    #     for book in self:
    #         # We have to be in sudo to have access to the images
    #         book_id = self.sudo().env['zerone.book'].browse(book.id)
    #         book.image_1920 = book_id.image_1920
    #         book.image_1024 = book_id.image_1024
    #         book.image_512 = book_id.image_512
    #         book.image_256 = book_id.image_256
    #         book.image_128 = book_id.image_128

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
