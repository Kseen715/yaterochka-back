#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv[:2])


if __name__ == '__main__':
    # run this command in terminal:
    params = sys.argv[1:]
    print(sys.argv[:2])
    try:
        # remove file if exists
        os.remove('db.conf')
    except:
        pass
    with open('db.conf', 'w') as f:
        f.write('\n'.join(params))

    main()
