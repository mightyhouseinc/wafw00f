#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'UTM Web Protection (Sophos)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if self.matchContent(r'www\.sophos\.com'):
        return True

    return bool(self.matchContent(r'Powered by.?(Sophos)? UTM Web Protection'))


def check_schema_02(self):
    if not self.matchContent(r'<title>Access to the requested URL was blocked'):
        return False

    if not self.matchContent(r'Access to the requested URL was blocked'):
        return False

    if not self.matchContent(r'incident was logged with the following log identifier'):
        return False

    if not self.matchContent(r'Inbound Anomaly Score exceeded'):
        return False

    return bool(self.matchContent(r'Your cache administrator is'))
