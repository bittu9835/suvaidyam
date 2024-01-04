// Copyright (c) 2023, Bittu and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle', {
    // Consider using a later event like 'render' or 'after_render' if necessary
    refresh: function (frm) {
        // Use console.log for debugging
        console.log("Setting placeholders for make and model fields");

        // Ensure correct field IDs
        var makeField = $("#make");
        var modelField = $("#model");
        console.log(makeField)

        // Set placeholders with appropriate text
        makeField.attr("placeholder", "Enter vehicle make");
        modelField.attr("placeholder", "Enter vehicle model");
    }
});
