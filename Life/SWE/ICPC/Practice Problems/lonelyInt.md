---
date: 2023-08-15
platform: HackerRank
problem-name: lonelyInt
difficulty: Basic
success-rate: 98.01%
language: Python
solved: False
topic: interview-prep
---
# Problem Description
From a list of integers, return the integer that is unique in the array.

## First Impression
I think this is going to be a hashmap/dict deal again, which I am notoriously bad at. Time to learn.

## Solution Notes
I was wrong again. Turns out the Python count function is really valuable. Should go back to learning that.

### Code Solution
```Python
import math
import os
import random
import re
import sys


def lonelyinteger(a):  
    for i in a:
        if a.count(i)==1:
            return i   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))  
    result = lonelyinteger(a)
    fptr.write(str(result) + '\n')  
    fptr.close()
```