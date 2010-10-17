#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 03 Jul 2009 16:58:58 CEST
DJANGO_SETTINGS_MODULE=portal.settings $(dirname $(dirname $0))/sw/bin/bitrepo_digest.py $1 "$2"
