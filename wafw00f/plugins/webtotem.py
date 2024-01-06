#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebTotem (WebTotem)'


def is_waf(self):
    return bool(
        self.matchContent(r"The current request was blocked.{0,8}?>WebTotem")
    )
