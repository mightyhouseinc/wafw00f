#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Tencent Cloud Firewall (Tencent Technologies)'


def is_waf(self):
    return bool(self.matchContent(r'waf\.tencent\-?cloud\.com/'))
