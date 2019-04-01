#!/usr/bin/env python

import sys
import time

def main():
    n = 0

    i = 3

    while i < 1000:
        n += i
        i += 3

    i = 5

    while i < 1000:
        if i % 3 != 0:
            n += i
        
        i += 5

    print(n)

if __name__ == "__main__":
    start = time.time()
    
    main()

    print("\ntime: {}".format(time.time() - start))

sys.exit()
