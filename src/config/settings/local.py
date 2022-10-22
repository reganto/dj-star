# flake8: noqa

from .base import *


DEBUG = get_env("DEBUG", default=True, cast=bool)
