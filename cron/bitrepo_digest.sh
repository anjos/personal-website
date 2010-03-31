#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 03 Jul 2009 16:58:58 CEST

source `dirname $0`/setup.sh
bitrepo_digest.py $1 "$2"
