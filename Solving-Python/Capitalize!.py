# This S0lving > دا هو الحل الي شغال
def solve(s):
    spliting = s.split()
    for name in spliting:
        s = s.replace(name,name.capitalize())
    return s

# --------------------------------
# دا الحل المثالي الي عملته ولكن مش شغال علي موقع Hackerrank
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    spliting = s.split()
    first_char = spliting[0][0]
    last_char = spliting[1][0]
    my_list = []
    
    if first_char != first_char.upper():
        uppers_first = first_char.upper()
        my_list.append(uppers_first)
        
    if first_char != False:
        my_list.append(spliting[0][1:])
        
    if last_char != last_char.upper():
        uppers_last = last_char.upper()
        my_list.append(uppers_last)
        
    if first_char != False:
        my_list.append(spliting[1][1:])
        
    first_p = my_list[0:2]
    last_p = my_list[2:]
    
    print("".join(first_p),"".join(last_p))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
