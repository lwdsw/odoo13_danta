# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       CAO.T.F
# Date:         2020-07-06 15:38
# Description:  

# -------------------------------------------------------------------------------

import json
from odoo import http



class NewestBooksController(http.Controller):
    @http.route('/newest_book', auth='public', website=True)
    def newest_book(self):
        book_obj = http.request.env['zerone.book'].sudo()
        # 这里的模板是 record: key = zerone_inherit.books_page
        return http.request.render('zerone_inherit.books_page', {
            'books': book_obj.search([], limit=5, order='id desc')
        })

    @http.route('/hello', auth='public', website=True)
    def print_hello_world(self):
        return '<h1>Hello, World!</h1>'

    @http.route('/hello/<name>', auth='public', website=True)
    def print_hello_name(self, name):
        return '<h1>Hello, {}!</h1>'.format(name)

    @http.route('/hello/<name>/<greetings>', auth='public', website=True)
    def print_greetings(self, **kw):
        return '<h1>Hello, {}! {} !</h1>'.format(kw.get("name"),kw.get("greetings"))
    
    @http.route('/find/book/<model("zerone.book"):book>/', auth='public', website=True)
    def find_a_book_by_id(self, book):
        return book.name

    @http.route('/book_list', type="http", auth='public', website=True, cors='*', csrf=False)
    def book_list(self, **kw):
        print(kw)
        book_obj = http.request.env['zerone.book']
        books = book_obj.sudo().search([], order='id desc')
        book_lst = []
        for book in books:
            book_lst.append({"id":book.id,"name":book.name})
        return json.dumps({"book_lst":book_lst})

    @http.route('/book_list/get', type="http", methods=["GET"], auth='public', website=True, cors='*', csrf=False)
    def book_list_only_get(self, **kw):
        print(kw)
        book_obj = http.request.env['zerone.book']
        books = book_obj.sudo().search([], order='id desc')
        book_lst = []
        for book in books:
            book_lst.append({"id":book.id,"name":book.name})
        return json.dumps({"book_lst":book_lst})


    @http.route('/book_list/get2', type="http", methods=["GET"], auth='public', website=True, cors='*', csrf=False)
    def book_list_only_get2(self):
        book_obj = http.request.env['zerone.book']
        books = book_obj.sudo().search([], order='id desc')
        book_lst = []
        for book in books:
            book_lst.append({"id":book.id,"name":book.name})
        return json.dumps({"book_lst":book_lst})
    
    @http.route('/book_list/post', type="http", methods=["POST"], auth='public', website=True, cors='*', csrf=False)
    def book_list_only_post(self, **kw):
        print(kw)
        book_obj = http.request.env['zerone.book']
        books = book_obj.sudo().search([], order='id desc')
        book_lst = []
        for book in books:
            book_lst.append({"id":book.id,"name":book.name})
        return json.dumps({"book_lst":book_lst})

    @http.route('/book_list/json', type="json", auth='public', website=True, cors='*', csrf=False)
    def book_list_json(self, **kw):
        print(kw)
        book_obj = http.request.env['zerone.book']
        books = book_obj.sudo().search([], order='id desc')
        book_lst = []
        for book in books:
            book_lst.append({"id":book.id,"name":book.name})
        return {"book_lst":book_lst}
