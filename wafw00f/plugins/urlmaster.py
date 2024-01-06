#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'URLMaster SecurityCheck (iFinity/DotNetNuke)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if self.matchHeader(('X-UrlMaster-Debug', '.+')):
        return True

    return bool(self.matchHeader(('X-UrlMaster-Ex', '.+')))


def check_schema_02(self):
    if not self.matchContent(r"Ur[li]RewriteModule"):
        return False

    return bool(self.matchContent(r'SecurityCheck'))
