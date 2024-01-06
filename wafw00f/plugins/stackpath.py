#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'StackPath (StackPath)'


def is_waf(self):
    return True if check_schema_01(self) else bool(check_schema_02(self))


def check_schema_01(self):
    if self.matchContent(r'<title>StackPath[^<]+</title>'):
        return True

    return bool(
        self.matchContent(
            r'Protected by <a href="https?:\/\/(?:www\.)?stackpath\.com\/"[^>]+>StackPath'
        )
    )


def check_schema_02(self):
    if not self.matchContent(r"is using a security service for protection against online attacks"):
        return False

    return bool(
        self.matchContent(
            r'An action has triggered the service and blocked your request'
        )
    )
