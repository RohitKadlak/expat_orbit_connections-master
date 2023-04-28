# Copyright (c) 2023, rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ConnectionRequest(Document):

	@frappe.whitelist()
	def accept(self):
		self.status = "Connected"
		self.save(ignore_permissions=True)

		mc_doc = frappe.get_value("My Connections",{'name':self.sender},['name'])
		if mc_doc:
			add_mc = frappe.get_doc("My Connections",{'name':self.sender})
			for mcl in add_mc.connections:
				if mcl.expat == self.receiver:
					frappe.msgprint("Already Connected")
				else:
					add_mc.append("connections",{
						"expat": self.receiver
					})
					add_mc.save(ignore_permissions=True)
					frappe.msgprint(f"Connect is added in {self.sender}")

		else:
			my_cunnection = frappe.new_doc("My Connections")
			my_cunnection.expat = self.sender
			my_cunnection.append("connections",{
				"expat": self.receiver
			})
			my_cunnection.save(ignore_permissions=True)
			frappe.msgprint("Create My Connection")

	@frappe.whitelist()
	def reject(self):
		self.status = "Rejected"
		self.save(ignore_permissions=True)