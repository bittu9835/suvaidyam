import frappe


def get_context(context):
    context.vehicle_list = frappe.get_list(
        "Vehicle",
        filters={"status": "Active"},
        fields=["make", "model", "year", "route", "vehicle_img"],
        order_by="make"
    )
