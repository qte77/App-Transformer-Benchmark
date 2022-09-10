#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Redirects to entrypoint of the app"""

from .app import main
from sys import exit

if __name__ == "__main__":
    exit(main())
