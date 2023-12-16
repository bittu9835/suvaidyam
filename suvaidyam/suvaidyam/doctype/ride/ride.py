# Copyright (c) 2023, Bittu and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Ride(Document):
	def validate(self):
		total_amount = 0.0
		
		for item in self.cost_breakup:
			item.amount = item.distance_in_km*item.rate_per_km
			total_amount += item.amount

		self.total_amount = total_amount