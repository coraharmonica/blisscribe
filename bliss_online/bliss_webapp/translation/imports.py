"""
PACKAGES:

    Holds packages for Blisscribe.
"""


def safe_import(pkg_name):
    exec("try:\n\timport {0}\nexcept ImportError:\n\tfrom bliss_online.bliss_webapp.translation import {0}".format(pkg_name))

