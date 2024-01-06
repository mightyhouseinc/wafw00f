#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DataPower (IBM)'


def is_waf(self):
    return bool(self.matchHeader(('X-Backside-Transport', r'(OK|FAIL)')))
