#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'DenyALL (Rohde & Schwarz CyberSecurity)'


def is_waf(self):
    if not self.matchStatus(200):
        return False

    return bool(self.matchReason('Condition Intercepted'))
