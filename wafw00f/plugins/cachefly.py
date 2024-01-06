#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'CacheFly CDN (CacheFly)'


def is_waf(self):
    if self.matchHeader(('BestCDN', r'Cachefly')):
        return True

    return bool(self.matchCookie(r'^cfly_req.*='))
