#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Sat 17 Oct 2010 14:49:00 CEST 

"""A module that facilitates using the website on a dreamhost based install.
"""

def setup():
  """Generic setup for any possible installation of this software."""
  import os

  # Makes sure we have the latest git available on our private installation
  os.environ.setdefault('HOME', '/home/andreps')
  home_bin = os.path.join(os.environ['HOME'], 'sw', 'bin')
  os.environ['PATH'] = ':'.join([home_bin, os.environ.get('PATH', '')])

  # Our time zone
  os.environ['TZ'] = 'Europe/Zurich'

def fcgi():
  """This will answer to the FCGI requests"""
  from django.core.servers.fastcgi import runfastcgi
  setup()
  runfastcgi(method="threaded", daemonize="false")
