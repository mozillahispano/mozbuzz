"""
WSGI config for formacion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os
import sys

configuration= os.path.dirname(__file__)
project = os.path.dirname(configuration)
workspace = os.path.dirname(project)

sys.path.append(workspace)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mozbuzz.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
