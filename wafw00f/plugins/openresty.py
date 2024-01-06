#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Open-Resty Lua Nginx (FLOSS)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if not self.matchHeader(('Server', r'^openresty/[0-9\.]+?')):
        return False

    return bool(self.matchStatus(403))


def check_schema_02(self):
    if not self.matchContent(r'openresty/[0-9\.]+?'):
        return False

    return bool(self.matchStatus(406))
