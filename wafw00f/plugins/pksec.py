#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'pkSecurity IDS (pkSec)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if self.matchContent(r'pk.?Security.?Module'):
        return True

    return bool(self.matchContent(r'Security.Alert'))


def check_schema_02(self):
    if not self.matchContent(r'As this could be a potential hack attack'):
        return False

    if not self.matchContent(r'A safety critical (call|request) was (detected|discovered) and blocked'):
        return False

    return bool(
        self.matchContent(
            r'maximum number of reloads per minute and prevented access'
        )
    )
