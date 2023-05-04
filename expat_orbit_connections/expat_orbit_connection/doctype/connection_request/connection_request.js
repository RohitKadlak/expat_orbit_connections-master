// Copyright (c) 2023, rohit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Connection Request', {
	refresh: function(frm) {
		frm.add_custom_button(__('Accept'), function() {
			frappe.call({
				method :'accept',
				doc:frm.doc,
				callback: function(r)
				{
				}
			});
		},__("Connection")),
		
		frm.add_custom_button(__('Reject'), function() {
			frappe.call({
				method :'reject',
				doc:frm.doc,
				callback: function(r)
				{
				}
			});
		},__("Connection"))
	}
});
