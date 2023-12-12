# Copyright (c) 2023, Bittu and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
    columns = [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data",
            "width": 150
        }
    ]

    data = [
        {"make": "BMW"},
        {"make": "TATA"}
    ]
    return columns, data
