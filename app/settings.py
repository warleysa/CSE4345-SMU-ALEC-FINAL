# Settings common to all environments (development|staging|production)
# Place environment specific settings in env_settings.py
# An example file (env_settings_example.py) can be used as a starting point

import os

# Application settings
APP_NAME = "SMU ALEC Tutor Site Demo"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " - system error"

# Flask settings
CSRF_ENABLED = True

# Flask-SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
