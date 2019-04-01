#!/usr/bin/env python

import sys
import time

def main():
    n = 0

    for i in range(1, 1000):
        if (i % 3 == 0) or (i % 5 == 0):
            n += i

    print(n)

if __name__ == "__main__":
    start = time.time()
    
    main()

    print("\ntime: {}".format(time.time() - start))

sys.exit()
