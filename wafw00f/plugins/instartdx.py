#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Instart DX (Instart Logic)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if self.matchHeader(('X-Instart-Request-ID', '.+')):
        return True

    if self.matchHeader(('X-Instart-Cache', '.+')):
        return True

    return bool(self.matchHeader(('X-Instart-WL', '.+')))


def check_schema_02(self):
    if not self.matchContent(r'the requested url was rejected'):
        return False

    if not self.matchContent(r'please consult with your administrator'):
        return False

    return bool(self.matchContent(r'your support id is'))
