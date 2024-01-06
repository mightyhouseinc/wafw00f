#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ServerDefender VP (Port80 Software)'


def is_waf(self):
    return bool(self.matchHeader(('X-Pint', r'p(ort\-)?80')))
