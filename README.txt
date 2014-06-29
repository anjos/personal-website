Personal Website
================

Setup::

  $ python bootstrap
  $ ./bin/buildout
  $ scp andreanjos@my.andreanjos.org:my.andreanjos.org/portal/dbconfig.py portal/
  $ ./helpers/copy.local.sh
  $ vim dbconfig.py # change db from server -> local
  $ scp -rC andreanjos@my.andreanjos.org:my.andreanjos.org/public static
