#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'wpmudev WAF (Incsub)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if not self.matchContent(r'href="http(s)?.\/\/wpmudev.com\/.{0,15}?'):
        return False

    if not self.matchContent(r'Click on the Logs tab, then the WAF Log.'):
        return False

    if not self.matchContent(r'Choose your site from the list'):
        return False

    return bool(self.matchStatus(403))


def check_schema_02(self):
    if not self.matchContent(r'<h1>Whoops, this request has been blocked!'):
        return False

    if not self.matchContent(r'This request has been deemed suspicious'):
        return False

    if not self.matchContent(r'possible attack on our servers.'):
        return False

    return bool(self.matchStatus(403))
