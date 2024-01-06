#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'WebKnight (AQTRONIX)'


def is_waf(self):
    if check_schema_01(self):
        return True

    return True if check_schema_02(self) else bool(check_schema_03(self))


def check_schema_01(self):
    return bool(self.matchReason('No Hacking')) if self.matchStatus(999) else False


def check_schema_02(self):
    if not self.matchStatus(404):
        return False

    return bool(self.matchReason('Hack Not Found'))


def check_schema_03(self):
    if self.matchContent(r'WebKnight Application Firewall Alert'):
        return True

    if self.matchContent(r'What is webknight\?'):
        return True

    if self.matchContent(r'AQTRONIX WebKnight is an application firewall'):
        return True

    if self.matchContent(r'WebKnight will take over and protect'):
        return True

    if self.matchContent(r'aqtronix\.com/WebKnight'):
        return True

    return bool(self.matchContent(r'AQTRONIX.{0,10}?WebKnight'))
