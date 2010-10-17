#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Qua 03 Mar 2010 11:13:25 CET 

"""Procedures to clean-up unused permissions and content types.
"""
import os, sys
activate = os.path.realpath(os.path.join(os.path.dirname(sys.argv[0]),
  '..', 'sw', 'bin', 'activate_this.py'))
execfile(activate, dict(__file__=activate))

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.db.models import get_model

debug = True
if len(sys.argv) > 1: debug = False

print "\nDeleting obsolete django 'permissions'...\n"

for k in Permission.objects.all():
  if not get_model(k.content_type.app_label, k.content_type.model):
    if debug: print '[debug] would delete: %s %s' % (k.id, k)
    else: 
      print 'deleting: %s %s' % (k.id, k)
      k.delete()

print "\nDeleting obsolete django 'content types'...\n"

for k in ContentType.objects.all():
  if not get_model(k.app_label, k.model):
    if debug: print '[debug] would delete: %s %s@%s (%s)' % \
      (k.id, k.model, k.app_label, k.name)
    else: 
      print 'deleting: %s %s@%s (%s)' % (k.id, k.model, k.app_label, k.name)
      k.delete()
