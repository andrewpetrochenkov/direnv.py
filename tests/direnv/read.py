#!/usr/bin/env python
import direnv
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

data = direnv.read()

assert data['key'] == 'value'
assert 'key' not in os.environ


data = direnv.read('sub-dir')

assert data['key'] == 'sub-value'
