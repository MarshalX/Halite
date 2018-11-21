#!/usr/bin/env python3
# Python 3.6

import pydevd
pydevd.settrace('localhost', port=2222, stdoutToServer=True, stderrToServer=True)

import MyBot
