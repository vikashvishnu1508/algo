#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(s):
    step = 0
    previous_Step = 0
    up = 0
    count = 0
    for i in s:
        if i == 'U':
            step += 1
        else:
            step -= 1
        if step <= 0 and previous_Step <= 0:
            if up == 1 and previous_Step > step:
                count += 1
                up = 0
            if previous_Step < step:
                up = 1
        previous_Step = step
    return count

s = 'DDUDDUUDUU'
print(countingValleys(s))