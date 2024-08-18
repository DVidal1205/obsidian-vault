---
date: 2023-08-14
platform: HackerRank
problem-name: plusMinus
difficulty: Basic
success-rate: 89.24%
language: Python
solved: True
topic: interview-prep
---
# Problem Description
Given an array of integers, print the following numbers up to a precision of 5 decimal places:
- The ratio of positive numbers in the array
- The ratio of negative numbers in the array
- The ratio of zeroes in the array
Example:
There are n=5 elements [1, 1, 0, -1, -1] in an array. Two positive, two negative, and one zero. The printed solution would be:
	Positive: 2/5 = 0.40000
	Negative: 2/5 = 0.40000
	Zeroes: 1/5 = 0.20000
	
## Solution Notes
- Make 3 arrays for each type of number, iterate over the array and append them to the proper array.
- Using the format(num, '.5f') Python command, print the len(arr) of the appropriate arrays in a ratio division.

### Code Solution
```Python
import re
import sys

def plusMinus(arr):

    # Positive Implementation
    positive =[]
    negative = []
    zeroes = []
    
    for num in arr:
        if num < 0:
            negative.append(num)
        elif num == 0:
            zeroes.append(num)
        elif num > 0:
            positive.append(num)

    print(format(len(positive)/len(arr), '.5f'))
    print(format(len(negative)/len(arr), '.5f'))
    print(format(len(zeroes)/len(arr), '.5f'))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
```
