#!/usr/bin/env python


#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Kona SiteDefender (Akamai)'


def is_waf(self):
    if self.matchHeader(('Server', 'AkamaiGHost')):
        return True

    return bool(self.matchHeader(('Server', 'AkamaiGHost'), attack=True))
