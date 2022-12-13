#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_rep = repr(number)
last_number = str_rep[-1]
last = int(last_number)
if last < 0:
    print(f"Last_digit of {number} is {last}")
    if last > 5:
        print("and is greater than 5")
    elif last == 0:
        print("and is 0")
    else:
        print("less than 6 and not 0")
