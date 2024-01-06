#!/usr/bin/env python3
'''
Copyright (C) 2023, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiGuard (Fortinet)'

def is_waf(self):
    return bool(check_schema(self))

def check_schema(self):
    if not self.matchContent('FortiGuard Intrusion Prevention'):
        return False

    if not self.matchContent('//globalurl.fortinet.net'):
        return False

    return bool(self.matchContent('<title>Web Filter Violation'))
