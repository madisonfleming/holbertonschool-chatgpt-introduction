#!/usr/bin/python3
import sys

def main():
print(sys.argv[0])
for arg in sys.argv[1:]: 
    print(arg)

if __name__ == "__main__":
    main()
