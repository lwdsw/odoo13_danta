# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       CAO.T.F
# Date:         2020-07-06 15:38
# Description:  

# -------------------------------------------------------------------------------

from odoo import http


class NewestBooksController(http.Controller):
    @http.route('/newest_book', auth='public', website=True)
    def newest_book(self):
        book_obj = http.request.env['zerone.book'].sudo()
        # 这里的模板是 record: key = zerone_inherit.books_page
        return http.request.render('zerone_inherit.books_page', {
            'books': book_obj.search([], limit=5, order='id desc')
        })
