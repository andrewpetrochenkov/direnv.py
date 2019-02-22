#!/usr/bin/env python
import env_file
import os
import public

@public.add
def read(path=None):
    """return a dictionary with environment variables depending on the current directory"""
    if not path:
        path = os.getcwd()
    result = dict()
    while os.path.dirname(path) != path:
        f = os.path.join(path, ".envrc")
        if os.path.exists(f) or os.path.lexists(f):
            vars = env_file.load(f)
            result.update(vars)
        path = os.path.dirname(path)
    return result


@public.add
def load(path=None):
    """load environment variables depending on the current directory"""
    vars = read(path)
    os.environ.update(vars)
    return vars
