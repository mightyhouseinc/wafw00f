#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Nemesida (PentestIt)'


def is_waf(self):
    if self.matchContent(r'@?nemesida(\-security)?\.com'):
        return True

    if self.matchContent(r'Suspicious activity detected.{0,10}?Access to the site is blocked'):
        return True

    return True if self.matchContent(r'nwaf@') else bool(self.matchStatus(222))
