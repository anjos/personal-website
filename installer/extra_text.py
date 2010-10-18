#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sun 28 Feb 19:52:16 2010 

"""A bunch of methods that will be added to the boostrap script. Please refer
to the virtualenv homepage for the explanation on those.
"""

import os, sys, subprocess

# Here we do some searches to see what we should enable/disable for local
# development.
def is_package(p): return os.path.exists(os.path.join(p, 'setup.py'))
LOCALS = [k for k in os.listdir(os.curdir) if is_package(k)]
LOCALS.append('.')

# My index
MY_INDEX = 'http://sw.andreanjos.org/git/simple/'

SOURCES = [
    #('git+http://github.com/simonw/django-openid.git', 'django-openid'),
    ]

def after_install(options, home_dir):
  """After everything is installed, this function is called.
  
  At this point, we populate our environment with all our goods.
  """
  if sys.platform == 'win32': bin = 'Scripts'
  else: bin = 'bin'

  # we first install pip, which is easier to use
  installer = [os.path.join(home_dir, bin, 'easy_install')] 
  subprocess.call(installer + ['pip'])
  
  installer = [os.path.join(home_dir, bin, 'pip'), 'install']
  #installer += ['--verbose', '--timeout=5']
  installer += ['--use-mirrors', '--extra-index-url=%s' % MY_INDEX]
  installer += ['--download-cache=downloads']
  if options.upgrade: installer.append('--upgrade')

  if SOURCES:
    sources = ['--editable=%s#egg=%s' % (k,k) for k in SOURCES]
    subprocess.call(installer + sources)

  for k in LOCALS: 
    #print 'Calling:', ' '.join(installer + ['--editable=%s' % k])
    subprocess.call(installer + ['--editable=%s' % k])

def extend_parser(parser):
  """Adds an upgrade option."""
  parser.add_option('-U', '--upgrade', action='store_true', dest='upgrade', 
    help='Use this if you want to upgrade instead of installing (default)')
