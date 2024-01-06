#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ChinaCache Load Balancer (ChinaCache)'


def is_waf(self):
    return bool(self.matchHeader(('Powered-By-ChinaCache', '.+')))
