#!/usr/bin/python3
x = 0
while x < 10:
    y = 0
    while y < 10:
        if y == 9 and x == 9:
            print("{}{}".format(x, y))
            break
        print("{}{}".format(x,y), end = ", ")
        y += 1
    x += 1
