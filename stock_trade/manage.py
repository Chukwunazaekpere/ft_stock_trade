#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv;


def main():
    """Run administrative tasks."""
    settings_module = "DJANGO_SETTINGS_MODULE"

    try:
        load_dotenv(
            os.path.join(os.path.dirname(__file__), "stock_trade", "config", "config.env")
        )
        os.environ.setdefault(settings_module, 'stock_trade.settings.dev_settings')

        if os.getenv(settings_module):
            os.environ[settings_module] = os.getenv(settings_module)

        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
