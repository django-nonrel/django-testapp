# -*- coding: utf-8 -*-
import logging, os, re, sys

base_path = os.path.abspath(os.path.dirname(__file__))

# Add checkpoints to patching procedure, so we don't apply certain patches
# multiple times. This can happen if an exeception gets raised on the first
# request of an instance. In that case, main.py gets reloaded and patch_all()
# gets executed yet another time.
done_patch_all = False

def patch_all():
    global done_patch_all
    if done_patch_all:
        return
    patch_python()
    setup_logging()
    done_patch_all = True

def patch_python():
    # Remove modules that we want to override. Don't remove modules that we've
    # already overridden.
    for module in ('memcache',):
        if module in sys.modules and \
                not sys.modules[module].__file__.startswith(base_path):
            del sys.modules[module]

def setup_logging():
    from django.conf import settings
    if settings.DEBUG:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)
