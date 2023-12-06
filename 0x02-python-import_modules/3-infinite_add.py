#!/usr/bin/python3
import sys

def add_arguments(argv):
    result = sum(int(arg) for arg in argv)
    print(result)

if __name__ == "__main__":
    add_arguments(sys.argv[1:])
