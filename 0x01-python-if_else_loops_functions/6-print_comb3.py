#!/usr/bin/python3
for tens in range(0, 10):
    for units in range(tens + 1, 10):
        if tens == 0 and units == 1:
            print("{}{}".format(tens, units))
        else:
            print("{:02d}, ".format(tens * 10 + units), end='')
print()
