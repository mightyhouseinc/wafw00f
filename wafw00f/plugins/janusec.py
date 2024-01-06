#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Janusec Application Gateway (Janusec)'


def is_waf(self):
    return bool(self.matchContent(r'janusec application gateway'))
