#!/usr/bin/python3
import sys
import os

for arg in sys.argv:
    print(os.path.basename(arg))
