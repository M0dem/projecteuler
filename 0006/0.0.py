#!/usr/bin/env python

import sys
import time

def main():
    n = 0
    s = 0
    for i in range(1, 100 + 1):
        n += i**2
        s += i

    print(s**2 - n)

if __name__ == "__main__":
    start = time.time()

    main()

    print("\ntime: {}s".format(time.time() - start))

sys.exit()
