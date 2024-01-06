#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'MaxCDN (MaxCDN)'


def is_waf(self):
    return bool(self.matchHeader(('X-CDN', r'maxcdn')))
