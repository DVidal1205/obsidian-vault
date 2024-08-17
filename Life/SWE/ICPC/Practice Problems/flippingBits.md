---
date: 2023-08-15
platform: HackerRank
problem-name: flippingBits
difficulty: Basic
success-rate: 97.62%
language: Python
solved: True
topic: interview-prep
---
# Problem Description


## First Impression
Not familiar with bit manipulation at all. Feeling doomed

## Solution Notes
As expected, this uses bit comprehension I don't quite understand

### Code Solution
```Python
import math
import os
import random
import re
import sys  

def flippingBits(n):
    return ~n & 0xFFFFFFFF

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') 
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
```