odoo.define('zerone.book.tree', function (require) {
    "use strict";

    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');

    var ZeroneBookListController = ListController.extend({
        buttons_template: 'ZeroneBook.buttons',
        events: _.extend({}, ListController.prototype.events, {
            'click .o_button_send_test': '_onButtonSend',
        }),
        _onButtonSend: function () {
            var self = this;
            var actived_ids = [];
            var state = self.model.get(self.handle, {raw: true});
            for (var i = 0; i < $('tbody .o_list_record_selector input').length; i++) {
                if ($('tbody .o_list_record_selector input')[i].checked === true) {
                    actived_ids.push(state.res_ids[i]);
                }
            }
            var ctx = state.context;
            ctx['active_ids'] = actived_ids;
            self.do_action({
                    type: "ir.actions.act_window",
                    name: "自定义按钮的动作",
                    res_model: "wizard.zerone",
                    views: [[false, 'form']],
                    target: 'new',
                    context: {
                        active_ids: actived_ids
                    },
                },
                {
                    on_reverse_breadcrumb: function () {
                        self.reload();
                    },
                    on_close: function () {
                        self.reload();
                    }
                }
            );
        }
    });

    var ZeroneBookListView = ListView.extend({
        config: _.extend({}, ListView.prototype.config, {
            Controller: ZeroneBookListController,
        }),
    });

    viewRegistry.add('zerone_book_tree', ZeroneBookListView);
});