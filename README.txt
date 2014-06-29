Personal Website
================

Setup::

  $ python bootstrap
  $ ./bin/buildout
  $ scp andreanjos@my.andreanjos.org:my.andreanjos.org/portal/dbconfig.py portal/
  $ ./helpers/copy.local.sh
  $ scp -rC andreanjos@my.andreanjos.org:my.andreanjos.org/public static
  $ vim portal/dbconfig.py # change db from server -> local
  $ vim portal/settings.py # change DREAMHOST -> False

