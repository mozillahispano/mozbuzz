===========================
Part 1: Contributor's Guide
===========================

============
Installation
============

Requirements
------------

To start developing and testing MozBuzz you will need:

 * Python_
 * Git_
 * PIP_
 * Virtualenv_

.. Note::

   If you use Linux or Mac then you surely already have Python installed.

.. _Python: http://python.org/
.. _Git: http://git-scm.com/
.. _PIP: http://www.pip-installer.org/
.. _Virtualenv: http://www.virtualenv.org/

Getting the code
----------------

First you need get a copy of the code::

    $ git clone https://github.com/mozillahispano/mozbuzz.git
    $ cd mozbuzz

Setup a virtual environment for the application
-----------------------------------------------

Create a new virtualenv to install MozBuzz dependencies without affecting other software in your machine::

  $ virtualenv env

If you are using any UNIX OS, you could also use VirtualenvWrapper_ for this.

.. _VirtualenvWrapper: http://virtualenvwrapper.readthedocs.org/en/latest/index.html

Install python packages
-----------------------

You'll need install python packages used in this project. These are in ``requirements.txt``.
The best way to install these packages is using ``pip``::

    $ pip install -r requirements/requirements.txt

Configuration
-------------
Start creating a ``settings_local.py``. You can use ``settings_local.py.example`` as a template.

Setup database::
	
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # mysql connection
            'NAME': 'mozbuzz', # database name
            'USER': 'root', # example
            'PASSWORD': 'mysql', # example
            'HOST': 'localhost',
            'PORT': '3306',
	    }
    }

    $ python manage.py syncdb
    $ python manage.py migrate

Run server::

    $ python manage.py runserver

Now you can open ``http://localhost:8000`` and see MozBuzz running.
