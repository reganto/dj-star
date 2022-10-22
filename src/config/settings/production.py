# flake8: noqa

from .base import *


DEBUG = get_env("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = get_env("ALLOWED_HOSTS")
