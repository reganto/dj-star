#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from decouple import config as get_env


def main():
    """Run administrative tasks."""
    DJANGO_ENV = get_env("DJANGO_ENV", default="local")
    SETTING_PATH = f"config.settings.{DJANGO_ENV}"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTING_PATH)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
