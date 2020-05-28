# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       CAO.T.F
# Date:         2020-05-26 9:33
# Description:  

# -------------------------------------------------------------------------------
{
    'name': "zerone_page_button_widget",
    'summary': """
            ·在【创建】【编辑】【导入】等自带的按钮后增加自定义按钮
            ·使Tree视图中的自定义按钮只有在勾选了记录的时候显示，就像动作、打印按钮一样
            ·使用Qweb Widget 实现
        """,
    'description': """
        ·在【创建】【编辑】【导入】等自带的按钮后增加自定义按钮
        ·使Tree视图中的自定义按钮只有在勾选了记录的时候显示，就像动作、打印按钮一样
    """,
    'author': "zerone",
    'category': 'tools',
    'version': '0.1',
    'depends': ['zerone_inherit'],
    'data': [
        'views/extend_view_assets.xml',
        'views/inherit_zerone_book.xml',
        'wizards/wizard_zerone.xml'
    ],
    'qweb': [
        "static/src/xml/view_button.xml"
    ],
    'installable': True,
    'application': True,
}
