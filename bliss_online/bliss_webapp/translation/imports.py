"""
IMPORTS:

    Holds import helpers for Blisscribe.
"""
import os, sys
PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PATH)
from importlib import import_module


module_prefix = 'bliss_online.bliss_webapp.translation'

try:
    import_module('..fonts', module_prefix + '.subpkg')
except ModuleNotFoundError:
    while len(module_prefix) != 0 and "." in module_prefix:
        module_prefix = module_prefix.split(".", maxsplit=1)[-1]
        try:
            import_module('..fonts', module_prefix + '.subpkg')
        except ModuleNotFoundError:
            continue
        else:
            break

MODULE_PREFIX = module_prefix + ".subpkg"


def safe_import(name):
    import_module(".." + name, MODULE_PREFIX)

