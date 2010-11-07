#!/bin/bash 
# Andre Anjos <andre.dos.anjos@gmail.com>
# Sat  6 Nov 18:43:44 2010

# This little application dumps the "server" database into the "local" database
# for testing purposes.
echo "Removing old copy..."
[ -r portal/local.sql3 ] && rm -f portal/local.sql3;
echo "Creating local database..." 
sw/bin/djm syncdb --database=local --noinput
echo "Resetting some apps..."
sw/bin/djm flush --database=local --noinput
sw/bin/djm reset --database=local --noinput auth contenttypes sites
echo "Copying all contents from remote server..."
sw/bin/djm dumpdata --database=server --indent=2 > tmp.json
sw/bin/djm loaddata --database=local tmp.json
echo "Done. Your local copy should be complete. Bye!"
rm -f tmp.json
