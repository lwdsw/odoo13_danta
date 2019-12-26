{
    'name': "zerone_books",
    'summary': """
        图书管理
        """,
    'description': """
        图书管理：
            图书信息
            图书分类信息
    """,
    'author': "zerone",
    'category': 'tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/zerone_book.xml',
        'views/zerone_tags.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
