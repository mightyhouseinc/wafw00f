#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AireeCDN (Airee)'


def is_waf(self):
    if self.matchHeader(('Server', 'Airee')):
        return True

    if self.matchHeader(('X-Cache', r'(\w+\.)?airee\.cloud')):
        return True

    return bool(self.matchContent(r'airee\.cloud'))
