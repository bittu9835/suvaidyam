# Copyright (c) 2023, Bittu and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
    def test_fullname_is_set_automatically(self):
        test_driver = frappe.get_doc({
            "doctype": "Driver",
            "first_name": "Bittu",
            "last_name": "Kumar",
            "dob": "2005-11-12"
        })
        test_driver.insert()
        self.assertEqual(test_driver.full_name, "Bittu Kumar")

    def test_fullname_is_set_without_last_name(self):
        test_driver = frappe.get_doc({
            "doctype": "Driver",
            "first_name": "Bittu",
            "dob": "2005-11-12"
        })
        test_driver.insert()
        self.assertEqual(test_driver.full_name, "Bittu")
