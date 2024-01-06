#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'LimeLight CDN (LimeLight)'


def is_waf(self):
    if self.matchCookie(r'^limelight'):
        return True

    return bool(self.matchCookie(r'^l[mg]_sessid='))
