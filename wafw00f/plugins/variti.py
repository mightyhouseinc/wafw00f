#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Variti (Variti)'

def is_waf(self):
    return bool(self.matchHeader(('Server', r'Variti(?:\/[a-z0-9\.\-]+)?')))
