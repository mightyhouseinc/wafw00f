#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BIG-IP AP Manager (F5 Networks)'


def is_waf(self):
    if check_schema_01(self):
        return True

    return True if check_schema_02(self) else bool(check_schema_03(self))


def check_schema_01(self):
    if not self.matchCookie('^LastMRH_Session'):
        return False

    return bool(self.matchCookie('^MRHSession'))


def check_schema_02(self):
    if not self.matchCookie('^MRHSession'):
        return False

    return bool(self.matchHeader(('Server', r'Big([-_])?IP'), attack=True))


def check_schema_03(self):
    if self.matchCookie('^F5_fullWT'):
        return True

    if self.matchCookie('^F5_fullWT'):
        return True

    return bool(self.matchCookie('^F5_HT_shrinked'))
