#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Azure Front Door (Microsoft)'


def is_waf(self):
    return bool(self.matchHeader(('X-Azure-Ref', '.+?')))
