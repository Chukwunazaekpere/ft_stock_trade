"""
WSGI config for factory_explorer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
load_dotenv(
    os.path.join(__file__, "config", "config.env")
)
settings_module = "DJANGO_SETTINGS_MODULE"
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(settings_module, 'stock_trade.settings.prod_settings')
if os.getenv(settings_module):
    os.environ[settings_module] = os.getenv(settings_module)

application = get_wsgi_application()
