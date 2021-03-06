#!/usr/bin/env python
import os
import sys

# Add the root to the path to support local testing with
# runserver / WSGI_APPLICATION
sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
