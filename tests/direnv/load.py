#!/usr/bin/env python
import os
import direnv

os.chdir(os.path.dirname(os.path.realpath(__file__)))

direnv.load()

assert os.environ['key'] == 'value'


direnv.load('sub-dir')

assert os.environ['key'] == 'sub-value'
