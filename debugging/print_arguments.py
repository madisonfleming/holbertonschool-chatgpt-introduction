#!/usr/bin/python3
import sys
import os

if __name__ == "__main__":
    print(os.path.basename(sys.argv[0]))
    for arg in sys.argv[1:]:
        print(arg)
