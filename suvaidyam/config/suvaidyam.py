# myapp/myapp/config/myapp.py

from __future__ import unicode_literals


def get_context(context):
    context['login_url'] = '/login'
    context['registration_url'] = '/registration'
