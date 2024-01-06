#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'LiteSpeed (LiteSpeed Technologies)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if not self.matchHeader(('Server', 'LiteSpeed')):
        return False

    return bool(self.matchStatus(403))


def check_schema_02(self):
    if self.matchContent(r'Proudly powered by litespeed web server'):
        return True

    return bool(self.matchContent(r'www\.litespeedtech\.com/error\-page'))
