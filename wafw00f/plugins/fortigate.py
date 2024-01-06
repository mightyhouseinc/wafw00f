#!/usr/bin/env python
'''
Copyright (C) 2023, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiGate (Fortinet)'

def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))

def check_schema_01(self):
    if not self.matchContent('//globalurl.fortinet.net'):
        return False

    return bool(self.matchContent('FortiGate Application Control'))

def check_schema_02(self):
    if not self.matchContent('Web Application Firewall'):
        return False

    if not self.matchContent('Event ID'):
        return False

    return bool(self.matchContent('//globalurl.fortinet.net'))
