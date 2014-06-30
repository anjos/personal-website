#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Fri 01 Oct 2010 12:07:59 CEST

"""Project setup.
"""

from setuptools import setup, find_packages

setup(

    name = "anjos.personal",
    version = "0.7.0",
    description="My personal website",
    license="FreeBSD",
    author='Andre Anjos',
    author_email='andre.dos.anjos@gmail.com',
    long_description=open('README.rst').read(),
    url='https://github.com/anjos/personal-website',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    namespace_packages=[
      "anjos",
      ],

    install_requires = [

      # pretty generic
      'setuptools',
      'pillow',
      'flup',
      'uuid',
      'mysql-python',
      'python-openid',

      # others
      'django-robots',
      'django-openid-auth',
      'django-maintenancemode',
      'django-rosetta',

      # mine
      'djangoogle',
      'django-flatties',
      'django-nav',
      'django-chords',

      ],

    entry_points = {
      'console_scripts': [
        ],
      },

    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Environment :: Web Environment',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python',
      ],

)
