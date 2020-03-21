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
    'depends': ['zerone_books'],
    'data': [
        'views/inherit_zerone_shelf.xml',
        'wizard/export_books_data.xml',
        'data/ir_sequence_data.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
