# Copyright (c) 2023, Bittu and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data",
            "width": 150
        },
        {
            'fieldname': 'currency',
            'label': ('Currency'),
            'fieldtype': 'Link',
            'options': 'Currency'
        },
        {
            "fieldname": "revenue",
            "label": "Revenue",
            "fieldtype": "Currency",
            "width": 100,
            'options': 'currency'
        }
    ]

    rides = frappe.get_all(
        "Ride", fields=["vehicle", "total_amount", "vehicle.make"])

    revenue_by_making = {}

    for ride in rides:
        if ride.make in revenue_by_making:
            revenue_by_making[ride.make] += ride.total_amount
        else:
            revenue_by_making[ride.make] = ride.total_amount

    data = [{"make": make, "revenue": revenue,"currency":"INR"}
            for make, revenue in revenue_by_making.items()]

    chart = get_chart(data)

    return columns, data, None, chart, None


def get_chart(data):
    return {
        "data": {
            "labels": [d["make"] for d in data],
            "datasets": [{"name": "revenue_by_make", "values": [d["revenue"] for d in data]}]
        },
        "type": "pie"
    }
