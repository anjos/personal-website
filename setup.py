#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Fri 01 Oct 2010 12:07:59 CEST 

"""Project setup.
"""

from setuptools import setup, find_packages
from portal.setuptools import develop

setup(

    name = "portal",
    version = "1.0",
    packages = find_packages(),

    # we also need all translation files and templates
    package_data = {
      'portal': [
        'templates/*.html',
        'templates/openid/*.html',
        'templates/admin/*.html',
        'templates/locale/*/LC_MESSAGES/django.po',
        'templates/locale/*/LC_MESSAGES/django.mo',
        'media/css/*.css',
        'media/img/*.png',
        'media/img/admin/*.jpg',
        'media/img/admin/*.gif',
        ],
      },

    entry_points = {
      'console_scripts': [
        'djm = portal.scripts.manage:main',
        ],
      'portal.scripts': [
        'dispatch.fcgi = portal.scripts.dreamhost:fcgi',
        ],
      },

    # replaces the "develop" target with my own, that extends it.
    cmdclass = {
      'develop': develop,
      },

    zip_safe=False,

    install_requires = [
      'setuptools',
      'mysql-python',
      'django>=1.2',
      'djangoogle',
      'nav', 
      'audit', 
      'uuid', 
      'flup', 
      'django-robots',
      'python-openid',
      'django-openid-auth',
      'django-flatties',
      'django-bitrepo',
      'djpro',
      'django-maintenancemode',
      'django-chords',
      'django-rosetta',
      ],

    # metadata for upload to PyPI
    author = "Andre Anjos",
    author_email = "andre.dos.anjos@gmail.com",
    description = "Provides a django project for my personal website",
    license = "PSF",
    keywords = "django website",
    url = "http://sw.andreanjos.org/git/personal-website",

)
