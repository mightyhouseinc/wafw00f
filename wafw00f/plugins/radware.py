#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AppWall (Radware)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if self.matchContent(r'CloudWebSec\.radware\.com'):
        return True

    return bool(self.matchHeader(('X-SL-CompState', '.+')))


def check_schema_02(self):
    if not self.matchContent(r'because we have detected unauthorized activity'):
        return False

    if not self.matchContent(r'<title>Unauthorized Request Blocked'):
        return False

    if not self.matchContent(r'if you believe that there has been some mistake'):
        return False

    return bool(self.matchContent(r'\?Subject=Security Page.{0,10}?Case Number'))
