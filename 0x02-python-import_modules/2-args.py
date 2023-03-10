#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} {}".format(len(sys.argv) - 1, "argument:"
              if len(sys.argv) == 2 else "arguments:"))
        for i, element in enumerate(sys.argv[1:]):
            print("{:d}: {:s}".format(i+1, element))
