#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebSEAL (IBM)'


def is_waf(self):
    if self.matchHeader(('Server', 'WebSEAL')):
        return True

    if self.matchContent(r"This is a WebSEAL error message template file"):
        return True

    return bool(
        self.matchContent(r"WebSEAL server received an invalid HTTP request")
    )
