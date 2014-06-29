#!/bin/bash 
# Andre Anjos <andre.dos.anjos@gmail.com>
# Sat  6 Nov 18:43:44 2010

# This little application dumps the "server" database into the "local" database
# for testing purposes.
echo "Removing old copy..."
[ -r portal/local.sql3 ] && rm -f portal/local.sql3;
echo "Creating local database..."
./bin/django syncdb --noinput --database=local
echo "Resetting some apps..."
./bin/django sqlflush --database=local
./bin/django reset --noinput --database=local auth contenttypes sites
echo "Copying all contents from remote server..."
./bin/django dumpdata --database=server --indent=2 > tmp.json
./bin/django loaddata --database=local tmp.json
echo "Done. Your local copy should be complete. Bye!"
rm -f tmp.json
