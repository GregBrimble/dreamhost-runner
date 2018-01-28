from importlib import import_module
import logging
from os import execl, getcwd
from os.path import relpath
from sys import argv, executable, exit, path

try:
    from config import INSTANCE, INTERPRETER, MODULE, PACKAGE
except ImportError:
    exit("Could not import `config.py`. Copy from `config.example.py` and edit as required.")

try:
    path.append(PACKAGE)
    application = getattr(import_module(MODULE), INSTANCE)
except ImportError:
    if relpath(executable, getcwd()) != INTERPRETER:
        try:
            logging.info("Switching interpreter to `%s`..." % INTERPRETER)
            execl(INTERPRETER, INTERPRETER, *argv)
        except OSError:
            exit("Virtual environment `%s` could not be found." % INTERPRETER)
    else:
        exit("Could not import `%s` from `%s`." % (INSTANCE, "%s.%s" % (PACKAGE, MODULE)))
except OSError:
    exit("Could not change working directory to `%s`." % PACKAGE)
