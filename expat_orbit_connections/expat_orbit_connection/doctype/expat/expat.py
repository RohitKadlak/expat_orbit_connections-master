# Copyright (c) 2023, rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Expat(Document):
	@frappe.whitelist()
	def connection_request(self):
		expat_list = frappe.get_all("Expat")
		for exp_list in expat_list:
			if exp_list.name != self.name:
				c_reuest = frappe.new_doc("Connection Request")
				c_reuest.sender = self.name
				c_reuest.receiver = exp_list.name 
				c_reuest.status = "Pending"
				c_reuest.save(ignore_permissions=True)
		frappe.msgprint("Send Connection Request")

