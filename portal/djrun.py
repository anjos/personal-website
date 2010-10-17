#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Sun 17 Oct 16:14:55 2010 

"""Allows plugins to declare entry points that will be executed taking into
consideration the Django settings of this project.

# Missing to make this setuptools extension work:
  1. Find out how to get access to the script directory for the installation
  (see function write_script)
  2. Find out how to hook the install_django_scripts(dist) into setuptools.
"""

import os, sys
import pkg_resources
from distutils import log

sys_executable = os.path.normpath(sys.executable)

script_text = """#!%(executable)r
# django-scripts: %(spec)r,%(group)r,%(name)r
__requires__ = '%(spec)r'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('%(spec)s', '%(group)r', '%(name)s')()
    )"""

def create_django_scripts(dist):
  spec = str(dist.as_requirement())
  group = 'django_scripts'
  executable = sys_executable
  for name, ep in dist.get_entry_map(group).items(): 
    yield(name, script_text % locals())

def write_script(script_name, contents):
  script_dir = ??
  log.info("Installing the Django script %s to %s", script_name, script_dir)
  target = os.path.join(script_dir, script_name)
  self.add_output(target)

  if not self.dry_run:
    pkg_resources.ensure_directory(target)
    f = open(target, 'wt')
    f.write(contents)
    f.close()
    os.chmod(target, 0755)

def install_django_scripts(dist):
  for args in create_django_scripts(dist): write_script(*args)
