import os
import sys


def fix(ff):
    module_dir = os.path.join(os.path.dirname(ff), os.path.pardir)
    abs_path = os.path.abspath(module_dir)
    if '__init__.py' not in os.listdir(abs_path):
        raise Exception('__init__.py missing in directory {}'.format(abs_path))
    while '__init__.py' in os.listdir(module_dir):
        module_dir = os.path.join(module_dir, os.pardir)
        abs_path = os.path.abspath(module_dir)
    else:
        abs_path = os.path.abspath(module_dir)
        sys.path.append(
            abs_path
        )
