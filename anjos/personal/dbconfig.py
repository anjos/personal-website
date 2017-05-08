#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Fri Oct  1 22:11:27 2010

"""Keep this file away from public visibility.
"""

import os

DATABASES = {
    'local': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(os.path.dirname(__file__), 'local.sql3')
      },
    }

DATABASES['default'] = DATABASES['local']
