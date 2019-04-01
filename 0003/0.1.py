#!/usr/bin/env python

import sys
import time

def isprime(n):
    for i in range(2, (n / 2) + 1):
        if n % i == 0:
            return False

    return True

def factors(n):
    f = [1, n]
    x = 2
   
    while x < ((n / 2) + 1):
        print("x: {}".format(x))

        a = n
        f.append(x)
        while a > 0:
            if a % x == 0:
                a /= x
                print("a: {}".format(a))
                f.append(a)

            else:
                break
        
        # find lowest prime divisible into `n`
        while x < (n / 2) + 1:
            x += 1
            while not isprime(x):
                x += 1

            if n % x == 0:
                break

    return(f)

def main():
    f = factors(4225)
    f.sort()
    print("f: {}".format(f))

if __name__ == "__main__":
    start = time.time()

    main()

    print("\ntime: {}".format(time.time() - start))

sys.exit()
