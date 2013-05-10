======================
 Roadmap para Mozbuzz
======================

Normas generales de versionamiento
----------------------------------

**Dependencias**: dentro de una misma versión mayor no deben haber cambios de
versión mayor en las dependencias para asegurar la estabilidad de los sistemas
que están en producción. Se considera aceptable la actualización de dependencias
solo en los casos de actualizaciones de seguridad y corrección de errores.

**Números de versión/Tags**: se sigue el esquema de Mayor.Menor.Revisión. La
*versión mayor* aumenta cuando se hacen cambios que requieran un proceso de
migración no automatizable y cuando se actualizan versiones mayores de *Django*.
La *version menor* aumenta cuando se incluyen nuevas características. Las
versiones menores impares serán inestables o de pruebas, y las pares de producción.
La *revisión* aumenta cuando se corrigen fallos sobre una versión menor, casos en
los que también se incluirán los cambios triviales (documentación, PEP8, ...)

**Issues**: cada issue estará asociado a un *milestone* en el `Issue Tracker <https://github.com/mozillahispano/mozbuzz/issues>`_

Etiquetado de código actual (Mayo 2013)
=======================================

El código de la aplicación actual se etiquetará como versión 0.9, y se comenzará
el trabajo para la versión 1.0.

Versión 1.0.0
=============

La versión *1.0.0* sentará una base para el desarrollo de las nuevas características
discutidas de forma gradual y por prioridad hacia la versión 2.0.

 * Estabilización de Login con Persona/django-browserid
 * Migración a Django 1.5
 * Issues:

   + `#4 <https://github.com/mozillahispano/mozbuzz/issues/4>`_ Style the "new report" form
   + `#6 <https://github.com/mozillahispano/mozbuzz/issues/6>`_ Author and origin name fields
   + Actualizar la documentación (`#6 <https://github.com/mozillahispano/mozbuzz/issues/6>`_, `#16 <https://github.com/mozillahispano/mozbuzz/issues/16>`_, `#17 <https://github.com/mozillahispano/mozbuzz/issues/17>`_, `#31 <https://github.com/mozillahispano/mozbuzz/issues/31>`_)
   + `#23 <https://github.com/mozillahispano/mozbuzz/issues/23>`_ Some characters aren't imported correctly (sometimes)
   + `#38 <https://github.com/mozillahispano/mozbuzz/issues/38>`_ Home URL redirects to mozilla-hispano.org

Versión 1.2.0
=============

 * Issues:

   + `#30 <https://github.com/mozillahispano/mozbuzz/issues/30>`_ Unable to delete mention from public UI
   + `#32 <https://github.com/mozillahispano/mozbuzz/issues/32>`_ Blank/Unknown option for Estimated Audience field
   + `#34 <https://github.com/mozillahispano/mozbuzz/issues/34>`_ Basic graphs

Versión 1.4.0
=============

 * Issues:

   + `#7 <https://github.com/mozillahispano/mozbuzz/issues/7>`_ Create a combobox to change UI language
   + `#8 <https://github.com/mozillahispano/mozbuzz/issues/8>`_ Spanish l10n
   + `#5 <https://github.com/mozillahispano/mozbuzz/issues/5>`_ Create a inline followup form
   + `#11 <https://github.com/mozillahispano/mozbuzz/issues/11>`_ Create a magic section to gather information from the web

Versión 1.6.0
=============

 * Issues:

   + `#6 <https://github.com/mozillahispano/mozbuzz/issues/6>`_ Author and origin name fields
   + `#10 <https://github.com/mozillahispano/mozbuzz/issues/10>`_ Style reports
   + `#26 <https://github.com/mozillahispano/mozbuzz/issues/26>`_ Add attached files to report

Versión 1.8.0
=============

**TBD**

Versión 2.0.0
=============

 * Django 1.6?
 * Playdoh?
 
