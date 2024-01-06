#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Yunsuo (Yunsuo)'


def is_waf(self):
    if self.matchCookie(r'^yunsuo_session='):
        return True

    return bool(self.matchContent(r'class=\"yunsuologo\"'))
