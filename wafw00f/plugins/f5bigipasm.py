#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BIG-IP AppSec Manager (F5 Networks)'


def is_waf(self):
    return True if check_schema_01(self) else bool(self.matchCookie(r'^TS.+?'))


def check_schema_01(self):
    if not self.matchContent('the requested url was rejected'):
        return False

    return bool(self.matchContent('please consult with your administrator'))
