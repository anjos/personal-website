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
  import %(settings)s
  setup_environ(%(settings)s)
  sys.exit(
      load_entry_point('%(spec)s', '%(group)s', '%(name)s')()
  )"""

class develop(_develop):

  def __init__(self, *args, **kwargs):
    _develop.__init__(self, *args, **kwargs)

  def run(self, *args, **kwargs):
    _develop.run(self, *args, **kwargs)
    settings = self.discover_django_settings()
    if settings: self.install_django_scripts(settings)
    else: log.warn('Not installing django.scripts -- entry-point django.settings is undefined')

  def discover_django_settings(self):
    possibilities = []
    group = 'django.settings'
    dists, errors = \
        pkg_resources.working_set.find_plugins(pkg_resources.Environment())
    for name, ep in self.dist.get_entry_map(group).items():
      spec = str(ep.dist.as_requirement())
      possibilities.append(ep)

    if len(possibilities) == 0: return None
    if len(possibilities) > 1:
      log.warn('Found more than 1 "django.settings" entry-point in your installation')
      for i, k in enumerate(possibilities):
        log.warn('Entry %d: %s', i, k.name)
      log.info('To avoid this warning, suppress the other entries in your project\'s setup')
    log.info('Using django settings "%s"', possibilities[0].module_name)
    return possibilities[0].module_name

  def install_django_scripts(self, settings):
    for args in self.create_django_scripts(settings): 
      self.write_django_script(*args)

  def create_django_scripts(self, settings):
    group = 'django.scripts'
    executable = sys_executable
    
    #all other packages
    dists, errors = \
        pkg_resources.working_set.find_plugins(pkg_resources.Environment())
    entry_points = {} 
    #print '## (django.scripts)', spec
    #to use this edit pip/__init__.py around line 224 and make it show stdout 
    #import pdb; pdb.set_trace()
    for dist in dists: entry_points.update(dist.get_entry_map(group))

    # myself
    entry_points.update(self.dist.get_entry_map(group))

    for name, ep in entry_points.iteritems(): 
      spec = str(ep.dist.as_requirement())
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

