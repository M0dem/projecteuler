#!/usr/bin/env python

import sys
import time

def isprime(n):
    i = 2
    while i < ((n / 2) + 1):
        if n % i == 0:
            return False
        
        i += 1

    #for i in range(2, (n / 2) + 1):
    #    if n % i == 0:
    #        return False

    return True

def factors(n):
    f = [1, n]
    
    for i in range(2, (n / 2) + 1):
        if n % i == 0:
            f.append(i)

    return(f)

def main():
    n = 600851475143
    i = 2
    p = i
    while i < ((n / 2) + 1):
        if n % i == 0:
            print(i)
            if isprime(i):
                p = i
                print("----------> {}".format(p))

        i += 1

    print(p)


if __name__ == "__main__":
    start = time.time()

    main()

    print("\ntime: {}".format(time.time() - start))

sys.exit()
