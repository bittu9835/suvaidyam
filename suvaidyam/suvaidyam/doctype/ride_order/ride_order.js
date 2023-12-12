// Copyright (c) 2023, Bittu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    refresh(frm) {
        if (frm?.doc?.status === "New") {
            frm?.add_custom_button("Reject", () => {
                frm?.set_value("status", "Rejected")
                frm.save();
            }, "Actions")
            frm?.add_custom_button("Accept & Create Ride ", () => {
                const dialog = new frappe.ui.Dialog({
                    title: 'Create Ride',
                    fields: [
                        {
                            "fieldtype": "Link",
                            "fieldname": "driver",
                            "label": "Select Driver",
                            "options": "Driver",
                            "reqd": 1
                        }
                    ],
                    primary_action_label: "Create",
                    primary_action: (data) => {
                        frm?.set_value("status", "Accepted")
                        frm.save();
                        const driver_name = data.driver
                        frappe.new_doc("Ride", {
                            vehicle: frm.doc.vehicle,
                            driver: driver_name
                        })
                    }
                })
                dialog.show();
            }, "Actions")
        }
    },
});
