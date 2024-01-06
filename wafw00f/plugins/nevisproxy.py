#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NevisProxy (AdNovum)'


def is_waf(self):
    if self.matchCookie(r'^Navajo'):
        return True

    return bool(self.matchCookie(r'^NP_ID'))
