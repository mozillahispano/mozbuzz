===========================
Part 1: Contributor's Guide
===========================

============
Installation
============

Requirements
------------
The only requirements are:

* Python
* git

.. Note::

   If you use Linux or Mac surely alredy have Python installed.

.. Note::

   It's recomendable too, use a virtual environment for python (``virtualenv`` or similars).

Getting the code
----------------
First you need get a copy of the code::

    $ git clone https://github.com/mozillahispano/mozbuzz.git
    $ cd mozbuzz

Install python packages
-----------------------
You'll need install python packages used in this project. These are in ``requeriments.txt``.
The best way to install these packages is using ``pip``::

    $ pip install -r requirements.txt

.. Note::

   I asume you have running your virtual environment.

Configuration
-------------
Start creating a ``settings_local.py``. You can copy ``settings_local.py.example`` and rename this.

Setup database::

    $ ./manage.py syncdb
    $ ./manage.py migrate

Run server::

    $ ./manage.py runserver

Now you can open ``http://localhost:8000`` and see MozBuzz running.
