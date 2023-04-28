// Copyright (c) 2023, rohit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Expat', {
	refresh: function(frm) {
		frm.add_custom_button(__('Send Connection Request'), function() {
			frappe.call({
				method :'connection_request',
				doc:frm.doc,
				
				callback: function(r)
				{
				}
			});
		})
	}
});
