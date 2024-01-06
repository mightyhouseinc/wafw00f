#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'HyperGuard (Art of Defense)'


def is_waf(self):
    return bool(self.matchCookie('^WODSESSION='))
