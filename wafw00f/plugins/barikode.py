#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Barikode (Ethic Ninja)'


def is_waf(self):
    return bool(self.matchContent(r'<strong>barikode<.strong>'))
