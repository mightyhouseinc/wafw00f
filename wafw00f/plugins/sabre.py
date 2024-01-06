#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Sabre Firewall (Sabre)'


def is_waf(self):
    if self.matchContent(r'dxsupport\.sabre\.com'):
        return True

    return bool(check_schema_01(self))


def check_schema_01(self):
    if not self.matchContent(r'<title>Application Firewall Error'):
        return False

    return bool(
        self.matchContent(
            r'add some important details to the email for us to investigate'
        )
    )
