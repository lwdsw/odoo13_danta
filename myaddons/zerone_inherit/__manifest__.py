{
    'name': "zerone_inherit",
    'summary': """
        继承学习
        """,
    'description': """
        继承学习：
            为书架增加新的字段
    """,
    'author': "zerone",
    'category': 'tools',
    'version': '0.1',
    'depends': ['zerone_books','website'],
    'data': [
        'views/inherit_zerone_shelf.xml',
        'views/assets.xml',
        'wizard/export_books_data.xml',
        'data/ir_sequence_data.xml',
        'static/src/xml/newest_books_templates.xml',
        'views/zerone_newest_books_pages.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
