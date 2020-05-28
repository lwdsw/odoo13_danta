# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       CAO.T.F
# Date:         2020-03-16 14:19
# Description:  

# -------------------------------------------------------------------------------
import base64
import io

from odoo import api, fields, models, _
import xlwt


class ExportBooksData(models.TransientModel):
    _name = "export.books.data"

    start_date = fields.Date(string="开始时间")
    end_date = fields.Date(string="结束时间")
    already_export = fields.Boolean(string='已导出')
    file_name = fields.Char(string='文件名称', store=True)
    xls_file = fields.Binary(string='点击下载数据汇总', attachment=True)

    @staticmethod
    def _get_tags_string(book):
        tags = book.tags_ids.mapped("name")
        tags_str = "、".join(tags)
        return tags_str

    # 返回header
    def _sheet_header(self):
        header_list = [
            ['图书编号', '图书名称', '作者', '出版时间', '标签']
        ]
        return header_list

    # 返回data
    def _sheet_content(self):
        content_list = []
        books = self.sudo().env['zerone.book'].search([
            ("publish_date", "<=", self.end_date),
            ("publish_date", ">=", self.start_date)
        ])

        for book in books:
            content_list.append([
                book.code,
                book.name,
                book.author,
                book.publish_date.strftime('%Y-%m-%d'),
                self._get_tags_string(book)
            ])
        return content_list

    def export_file(self):
        result = self._sheet_header() + self._sheet_content()
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        # 居中
        al = xlwt.Alignment()
        al.horz = 0x02
        al.vert = 0x01
        style.alignment = al
        # 外边框
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        borders.bottom_colour = 0x3A
        style.borders = borders
        # 字体
        font = xlwt.Font()
        font.name = u'微软雅黑'
        font.height = 220
        style.font = font

        for i in range(len(result)):
            for j in range(len(result[i])):
                sheet.write(i, j, result[i][j], style)

        fp = io.BytesIO()
        wbk.save(fp)
        fp.seek(0)
        data = fp.read()
        fp.close()

        file_name = "%s-%s 图书数据.xls" % (str(self.start_date), str(self.end_date))
        self.write({'already_export': True, 'xls_file': base64.b64encode(data), 'file_name': file_name})
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'export.books.data',
            'target': 'new',
            'res_id': self.id,
        }
