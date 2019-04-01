#!/usr/bin/env python

import sys
import time

def main():
    n = 0

    i = 1
    j = 2

    while j < 4000000:
        if j % 2 == 0:
            n += j

        k = j
        j += i
        i = k 

    print(n)

if __name__ == "__main__":
    start = time.time()

    main()

    print("\ntime: {}".format(time.time() - start))

sys.exit()
