#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function, unicode_literals

from .base import Optimizer, RandomSearch

try:
    from .smac3 import SMAC3
except ImportError:
    print('WARNING: SMAC not found')

try:
    from .robo_wrapper import RoBO
except ImportError:
    print('WARNING: RoBO not found')
