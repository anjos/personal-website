#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Fri 01 Oct 2010 12:07:59 CEST

"""Project setup.
"""

from setuptools import setup, find_packages

setup(

    name = "portal",
    version = "0.6.0",
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

    zip_safe=False,

    install_requires = [
      'mysql-python',
      'django>=1.4',
      'djangoogle',
      'django-nav',
      'uuid',
      'flup',
      'django-robots',
      'python-openid',
      'django-openid-auth',
      'django-flatties',
      'django-bitrepo',
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
    url = "https://github.com/anjos/personal-website",

)
