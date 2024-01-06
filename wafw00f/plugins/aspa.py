#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ASPA Firewall (ASPA Engineering Co.)'


def is_waf(self):
    if self.matchHeader(('Server', r'ASPA[\-_]?WAF')):
        return True

    return bool(self.matchHeader(('ASPA-Cache-Status', r'.+?')))
