#!/usr/bin/env python

# 913, 993 > 906609

import sys
import time

def is_pal(n):
    return str(n) == str(n)[::-1]

def largest_pal(x, y):
    i = y
    j = y
    lp = 0
    while i > x:
        while j > 1:
            a = i * j
            if is_pal(a):
                print("i: {}\nj: {}\na: {}".format(i, j, a))
                if a > lp:
                    lp = a

            j -= 1

        i -= 1
        j = y

    return lp

def main():
    n = largest_pal(100, 999)
    print(n)

if __name__ == "__main__":
    start = time.time()

    main()

    print("\ntime: {}".format(time.time() - start))

sys.exit()
