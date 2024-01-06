#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Reblaze (Reblaze)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if self.matchCookie(r'^rbzid'):
        return True

    return bool(self.matchHeader(('Server', 'Reblaze Secure Web Gateway')))


def check_schema_02(self):
    if not self.matchContent(r'current session has been terminated'):
        return False

    if not self.matchContent(r'do not hesitate to contact us'):
        return False

    return bool(self.matchContent(r'access denied \(\d{3}\)'))
