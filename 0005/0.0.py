#!/usr/bin/env python

import sys
import time

def main():
    i = 20
    x = 1
    while True:
        if len(str(i)) > x:
            x = len(str(i))

        print(x)
        div = True
        for j in range(1, 20 + 1):
            if i % j != 0:
                div = False
                continue

        if div:
            break

        i += 1

    print(i)

if __name__ == "__main__":
    start = time.time()

    main()

    print("\ntime: {}s".format(time.time() - start))

sys.exit()
