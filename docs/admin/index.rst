=============================
Part 2: Administrator's Guide
=============================

.. Note::

   This is a work in progress and may have errors.

Installation
============

This guide assumes you are installing the application code into `/var/lib/mozbuzz` and the public files into `/var/www/mozbuzz`.

Cloning
-------

Get the application files into the destination folder by clonning the `MozBuzz public Git repository`_::

  $ cd /var/lib
  $ git clone https://github.com/mozillahispano/mozbuzz.git

Setting up the execution environment
------------------------------------

You will need a Python `virtualenv`_ to hold Mozbuzz dependencies::

  $ pip install -U virtualenv
  $ cd /var/lib/mozbuzz
  $ virtualenv .
  $ source bin/activate
  $ pip install -r requirements/production.txt

Set up the site
---------------

An example setup can be found in `settings_local.py.example`. Copy that to `settings_local.py` and customize your settings. Pay special attention to the `DATABASES` and `STATIC_ROOT` settings.

Create the application's database tables by running::

  $ python manage.py syncdb


Copy the files at `public/` to `/var/www/mozbuzz` and collect the static files::

  $ python manage.py collectstatic

Set up the webserver
--------------------

You should refer to your webserver's documentation to find how to setup the site. We recommend running the site using Nginx_ and uWSGI_.

Nginx
~~~~~

Create a virtualhost at `/etc/nginx/sites-enabled/mozbuzz`::

  server {
    listen  80;
    server_name mozbuzz.mozilla-hispano.org;
    access_log /var/log/nginx/mozbuzz.mozilla-hispano.org.access.log;
    error_log /var/log/nginx/mozbuzz.mozilla-hispano.org.error.log;

    location / {
      uwsgi_pass unix:///tmp/mozbuzz.mozilla-hispano.org.sock;
      include uwsgi_params;
    }

    location /media/ {
      alias /var/www/mozevents/public/media/;
    }
    
    location /static/ {
      alias /var/www/mozevents/static/;
    }
  }

uWSGI
~~~~~

Create an uWSGI app at `/etc/uwsgi/apps-enabled/mozbuzz.mozilla-hispano.org.ini`::

  [uwsgi]
  vhost = true
  plugins = python
  socket = /tmp/mozbuzz.mozilla-hispano.org.sock
  master = true
  enable-threads = true
  processes = 2
  wsgi-file = /var/www/mozbuzz/public/wsgi_handler.py
  virtualenv = /var/www/mozbuzz/
  chdir = /var/www/mozbuzz

Restart the Nginx and uWSGI services and enjoy.

.. _MozBuzz public Git repository: https://github.com/mozillahispano/mozbuzz/
.. _virtualenv: https://www.virtualenv.org/en/latest/
.. _Nginx: https://nginx.org
.. _uWSGI: https://uwsgi-docs.readthedocs.org/en/latest/

Upgrade
=======

Before an upgrade please test you current setup with the new code. Look at the configuration examples and the documentation to find if you need to update your setup after the upgrade.

Install new dependencies and upgrades, if any::

  $ pip install -U -r requirements/production.txt

Always run database migrations after an upgrade by issuing in a command line::

  $ python manage.py migrate

Also, make sure your static assets are up to date by running::

  $ python manage.py collectstatic
