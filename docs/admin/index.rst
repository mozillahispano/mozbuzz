=============================
Part 2: Administrator's Guide
=============================

.. Note::

   This is a work in progress and may have errors.

Installation
============

Get the application files by clonning the `MozBuzz public Git repository`_::

  $ git clone https://github.com/mozillahispano/mozbuzz.git

.. Warning::

   Do not put all the source files inside the webserver's public folder. Rather use the wsgi script provided in the sources at `mozbuzz/wsgi.py`.

.. _MozBuzz public Git repository: https://github.com/mozillahispano/mozbuzz/

Upgrade
=======

Before an upgrade please test you current setup with the new code. Look at the configuration examples and the documentation to find if you need to update your setup after the upgrade.

Always run database migrations after an upgrade by issuing in a command line::

  $ python manage.py migrate

Also, make sure your static assets are up to date by running::

  $ python manage.py collectstatic

Administration
==============

TODO
