"""
WSGI config for tercera_pre_entrega_jacobi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tercera_pre_entrega_jacobi.settings')

application = get_wsgi_application()
