from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import get_fullname
import json


@frappe.whitelist(allow_guest=True)
def register_user(data):
    try:
        user = frappe.new_doc('User')
        user.update(json.loads(data))
        user.update({
            'doctype': 'User',
            'user_type': 'System User',
            'send_welcome_email': 0,
            'enabled': 1,
            # Assign the appropriate role
            # 'roles': [{'role': 'student'}],
            "role_profile_name": "student"
        })
        user.insert(ignore_permissions=True)

        frappe.msgprint(_('Registration successful.'))
        return 'success'
    except frappe.DuplicateEntryError:
        frappe.msgprint(_('Email already registered.'))
        return 'duplicate'
    except Exception as e:
        frappe.msgprint(_('Error during registration: {0}').format(str(e)))
        return 'error'
