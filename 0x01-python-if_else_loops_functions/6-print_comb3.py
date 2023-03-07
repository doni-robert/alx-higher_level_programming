#!/usr/bin/python3

for i in range(0, 10):
    if i != 8:
        for n in range(0, 10):
            if n > i:
                print("{}{}, " .format(i, n), end="")
    else:
        print("{}{}" .format(i, n))
