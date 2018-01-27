from importlib import import_module
import logging
import os
from sys import argv, executable, exit

try:
    from config import INSTANCE, INTERPRETER, MODULE, PACKAGE
except ImportError:
    exit("Could not import `config.py`. Copy from `config.example.py` and edit as required.")

try:
    application = getattr(import_module("%s.%s" % (PACKAGE, MODULE)), INSTANCE)
    # from boilerplate_web_service.app import app as application
except ImportError:
    if os.path.relpath(executable, os.getcwd()) != INTERPRETER:
        try:
            logging.info("Switching interpreter to `%s`..." % INTERPRETER)
            os.execl(INTERPRETER, INTERPRETER, *argv)
        except OSError:
            exit("Virtual environment `%s` could not be found." % INTERPRETER)
    else:
        exit("Could not import `%s` from `%s`." % (INSTANCE, "%s.%s" % (PACKAGE, MODULE)))
