#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FirePass (F5 Networks)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if not self.matchCookie('^VHOST'):
        return False

    return bool(self.matchHeader(('Location', r'\/my\.logon\.php3')))


def check_schema_02(self):
    if not self.matchCookie(r'^F5_fire.+?'):
        return False

    return bool(self.matchCookie('^F5_passid_shrinked'))
