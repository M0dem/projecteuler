#!/usr/bin/env python

# -1

import sys
import time

def main():
    n = 0

    i = 3
    j = 5

    while i < 1000:
        n += i
        if (j % 3 != 0) and (j < 1000):
            n += j

        i += 3
        j += 5

    print(n)

if __name__ == "__main__":
    start = time.time()
    
    main()

    print("\ntime: {}".format(time.time() - start))

sys.exit()
