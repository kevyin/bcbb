"""Allows subprocess calls to be autmatically logged
   eg: subprocess_logged.check_call()
"""
import sys
import inspect
from bcbio.log import logger_subprocess
import subprocess
from functools import wraps

subprocess_logged = sys.modules[__name__]

def logcall(func):
    @wraps(func)
    def _exec(*args, **kw):
        logger_subprocess.info(" ".join(args[0]))
        return func(*args, **kw)
    return _exec

for func, v in inspect.getmembers(subprocess, inspect.isroutine):
    setattr(subprocess_logged, func, logcall(v))

