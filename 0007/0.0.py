#!/usr/bin/env python

import sys
import time

def is_prime(n):
    i = 2
    while i < ((n / 2) + 1):
        if n % i == 0:
            return False

        i += 1

    return True

def main():
    i = -1
    j = 0
    while i <= 10001:
        j += 1
        if is_prime(j):
            i += 1
        
    print(j, i)

if __name__ == "__main__":
    start = time.time()

    main()

    print("\ntime: {}s".format(time.time() - start))

sys.exit()
