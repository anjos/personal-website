===============================
 Andre Anjos' Personal Website
===============================

This package contains the source and deployment instructions for my personal
website. The latest version is available from `my github website
<http://github.com/anjos/personal-website>`.

Installation
------------

Clone this package using the following command::

  $ git clone git@github.com:anjos/personal-website
  $ git submodule init
  $ git submodule update

After that, bootstrap the environment::

  $ python bootstrap.py
  $ ./bin/buildout

By default, the settings on the project are setup to work with a local
``db.sql3`` that should be placed at the root of the package. You can also work
against a MySQL server. In such a case, you will need to get hold of the MySQL
connection string. You can copy the one on your private server, if you have the
right to do so::

  $ scp andreanjos@andreanjos.org:my.andreanjos.org/anjos.personal/anjos/personal/dbconfig.py anjos/personal

Otherwise, here is a template (it should be placed on the same directory as
``settings.py`` is)::

  import os

  DATABASES = {
      'local': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'local.sql3')
        },
      'server': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database-name>',
        'USER': '<database-user>',
        'PASSWORD': '*********',
        'HOST': 'mysql.andreanjos.org',
        'PORT': '3306',
        },
      }

  DATABASES['default'] = DATABASES['server']

.. warning::

  Make sure you don't make the above file public, or checks it into the git
  repository. It contains sensitive data (username, password and the database
  server address).

Next, you will need to copy media only available remotely, to the current
working directory and collect all apps static files::

  $ ./bin/dj collectstatic --noinput
  $ rsync -avz andreanjos@my.andreanjos.org:my.andreanjos.org/public/media/ media/

Maintenance
-----------

Here are some common tips for maintenance.

Running a Test Server
=====================

You can run a test server locally, either using the remote (Dreamhost) default
MySQL database or a local version. To start a test server::

  $ ./bin/dj runserver

To setup a local copy of the MySQL database, look below.

Removing Obsolete Apps
======================

This happens when you remove applications from your website::

  $ ./bin/remove_app.py <appname>

Debugging 500 Errors
====================

To debug 500 errors, add the egg ``paste`` to your buildout, then edit,
manually, the file ``./bin/dj.wsgi`` to add the following two lines, by the
end::

  import djangorecipe.wsgi
  from paste.exceptions.errormiddleware import ErrorMiddleware #<< add this
  application = djangorecipe.wsgi.main('anjos.personal.settings', logfile='')
  application = ErrorMiddleware(application, debug=True) #<< add this

Make sure to kill the current webserver process being run::

  $ pkill python

And to touch ``<webserver-folder>/tmp/restart.txt``::

  $ touch tmp/restart.txt

Now try to reload the page you had problems with and observe the logs being
displayed on the web browser screen.

Moving a MySQL database to SQLite3
==================================

To work locally, using an SQLite database for development, you can dump the
current data on your server and load it again on a local sqlite3 database::

  $ ./bin/dj dumpdata > data.json
  $ vim anjos/personal/dbconfig.py # change to the local database configuration
  $ ./bin/dj syncdb --noinput
  $ ./bin/dj reset auth --noinput
  $ ./bin/dj reset contenttypes --noinput
  $ ./bin/dj loaddata data.json
  $ rm -f data.json

Installing on Dreamhost
=======================

Follow these steps:

1. Make sure that the database configuration is set right;

2. Make sure that the variable ``DREAMHOST`` is set to ``True`` at the top of
   the ``settings.py`` file. Do the same for ``DEBUG`` (setting it to
   ``False``);

3. Link ``passenger_wsgi.py``::
   $ cd <website-directory>
   $ ln -s anjos.website/bin/dj.wsgi passenger_wsgi.py

4. Set up the backup cronjob to execute daily (e.g.: ``backup/do_it.sh``). Here
   is an example::

     #!/bin/sh
     cd `dirname $0`
     mysqldump -h mysql.andreanjos.org -u aadjadmin -p******* --opt aa_professional_website > db.sql
     /usr/sbin/logrotate --state=logrotate.state logrotate.conf

5. If you cleaned-up the previous installation, run ``dj collectstatic
   --noinput`` to re-issue the static files on the adequate location.
