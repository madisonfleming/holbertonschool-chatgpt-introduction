#!/usr/bin/python3
import sys
import os

if __name__ == "__main__":
    for arg in sys.argv:
        print(os.path.basename(arg))
