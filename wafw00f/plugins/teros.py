#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Teros (Citrix Systems)'


def is_waf(self):
    return bool(self.matchCookie(r'^st8id='))
