# Copyright (c) 2023, Bittu and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestRide(FrappeTestCase):
    def setUp(self):
        frappe.get_doc({
            "doctype": "Driver",
            "first_name": "Bittu",
            "dob": "2005-11-12"
        }).insert()

    frappe.get_doc({
        "doctype": "Vehicle",
        "make": "Mercedes",
        "model": "C-Class",
        "Active": "active"
    }).insert()

    def test_ride_total_amount_calculation(self):
        test_driver = frappe.get_doc({
            "doctype": "Ride",
            "vehicle": "BMW",
            "driver": "Bittu",
            "cost_breakup": [
                {"source": "Bansdih",
                 "destination": "Office",
                 "distance_in_km": 10,
                 "rate_per_km": 5,
                 "amount": 50},
                {"source": "Bansdih",
                 "destination": "Office",
                 "distance_in_km": 5,
                 "rate_per_km": 4,
                 "amount": 20}
            ]
        })
        test_driver.insert()
        self.assertEqual(test_driver.total_amount, 70)
