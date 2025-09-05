#!/usr/bin/python3
import sys
import os

def main():
    print(os.path.basename(sys.argv[0]))
    for arg in sys.argv[1:]: 
        print(arg)


if __name__ == "__main__":
    main()
