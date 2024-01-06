#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'FortiWeb (Fortinet)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if self.matchCookie(r'^FORTIWAFSID='):
        return True

    return bool(self.matchContent('.fgd_icon'))


def check_schema_02(self):
    if not self.matchContent('fgd_icon'):
        return False

    if not self.matchContent('web.page.blocked'):
        return False

    if not self.matchContent('url'):
        return False

    if not self.matchContent('attack.id'):
        return False

    if not self.matchContent('message.id'):
        return False

    return bool(self.matchContent('client.ip'))
