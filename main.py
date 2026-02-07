#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    subtotal = 0
    divisor = 0
    counter = 0

    for entry in responseTimes:
        subtotal += int(entry)
        divisor += 1
        print("Average: ", subtotal // divisor)
        if entry > subtotal // divisor:
            counter += 1

    return counter

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
