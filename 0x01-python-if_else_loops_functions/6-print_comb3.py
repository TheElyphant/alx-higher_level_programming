#!/usr/bin/python3
for tens in range(10):
    for units in range(tens + 1, 10):
        if tens == 8 and units == 9:
            print("{}{}".format(tens, units))
        else:
            print("{:02d}".format(tens * 10 + units), end=', ')
