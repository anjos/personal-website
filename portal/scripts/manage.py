#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Sat 02 Oct 2010 08:56:06 CEST 

"""A module that facilitates managing the site.
"""

def main():
  from django.core.management import execute_manager
  from portal import settings
  execute_manager(settings)
