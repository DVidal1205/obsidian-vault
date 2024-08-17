---
date: 2023-08-14
platform: HackerRank
problem-name: timeConversion
difficulty: Basic
success-rate: 94.35%
language: Python
solved: True
topic: interview-prep
---
# Problem Description
Convert standard time to military time.
Example: s = '12:01:00AM'
	return: '00:01:00'
## First Impression
This one seems a bit trickier than the rest from today, mainly the PM and AM handling is throwing me off. If I had to guess, I will use a strip() function to split up the time.
## Solution Notes
This one was definitely a bit more tricky working with the split method. For future reference, split creates a new list, but does not modify the string to begin with. I needed to add an equation to work with the split list. Also, string to int conversion played a big role here, and was quite pesky.

Update: I did not factor in the AM as an alternative, code tests break whenever it is in the AM. I need to work on string comprehension

### Code Solution
```Python
import math
import os
import random
import re
import sys


def timeConversion(s):
    time = s[:8]
    am_pm = s[8:]
    h,m,sec = time.split(':')
    if am_pm =='PM' and int(h) < 12 :
        h = str(int(h) + 12)
    elif am_pm == 'AM' and int(h) == 12:
        h = '00'
    return (h+s[2:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = timeConversion(s) 

    fptr.write(result + '\n')

    fptr.close()
```
