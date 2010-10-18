#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Sun 17 Oct 16:14:55 2010 

"""Allows plugins to declare entry points that will be executed taking into
consideration the Django settings of this project.
"""

import os, sys
import pkg_resources
from distutils import log
from setuptools.command.develop import develop as _develop

sys_executable = os.path.normpath(sys.executable)

script_text = """#!%(executable)s
# django-scripts: %(spec)r,%(group)r,%(name)r
__requires__ = '%(spec)s'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
  from django.core.management import setup_environ
  from portal import settings
  setup_environ(settings)
  sys.exit(
      load_entry_point('%(spec)s', '%(group)s', '%(name)s')()
  )"""

class develop(_develop):

  def __init__(self, *args, **kwargs):
    _develop.__init__(self, *args, **kwargs)

  def run(self, *args, **kwargs):
    _develop.run(self, *args, **kwargs)
    self.install_django_scripts()

  def install_django_scripts(self):
    for args in self.create_django_scripts(): self.write_django_script(*args)

  def create_django_scripts(self):
    group = 'portal.scripts'
    executable = sys_executable
    dists, errors = \
        pkg_resources.working_set.find_plugins(pkg_resources.Environment())
    for dist in dists:
      spec = str(dist.as_requirement())
      #print '##', spec
      #to use this edit pip/__init__.py around line 224 and make it show stdout 
      #import pdb; pdb.set_trace()
      for name, ep in dist.get_entry_map(group).items():
        yield(name, script_text % locals())

    # also for myself!
    spec = str(self.dist.as_requirement())
    for name, ep in self.dist.get_entry_map(group).items():
      yield(name, script_text % locals())

  def write_django_script(self, script_name, contents):
    log.info('Installing %s (django) script to %s', script_name,
        self.script_dir)
    target = os.path.join(self.script_dir, script_name)
    self.add_output(target)

    if not self.dry_run:
      pkg_resources.ensure_directory(target)
      f = open(target, 'wt')
      f.write(contents)
      f.close()
      os.chmod(target, 0755)

