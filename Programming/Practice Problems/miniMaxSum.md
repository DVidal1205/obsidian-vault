---
date: 2023-08-14
platform: HackerRank
problem-name: miniMaxSum
difficulty: Basic
success-rate: 93.80%
language: Python
solved: True
topic: interview-prep
---
# Problem Description
Given an integer of five positive numbers, find the largest and smallest sums of 4 of the numbers. Then, print the smallest and largest sums on the same line.
Example: [1, 3, 5, 7, 9]
	Largest: 3 + 5 + 7 + 9 = 24
	Smallest: 1 + 3 + 5 + 7 = 16
	Output: 16 24

## First Impression
- Seems pretty easy, going to remove the largest and smallest from the array and add together
## Solution Notes
- As expected. I sorted the array, and found the largest and smallest of the array. Then, I added the entire array to find the base case sum, and subtracted the largest num to find the smallest sum. Inversely, I subtracted the smallest number to find the largest sum.
### Code Solution
```Python
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr.sort()
    smallest = arr[0]
    largest = arr[-1]
    arrSum = sum(arr)
    print((arrSum - largest), (arrSum - smallest))


if __name__ == '__main__':
    
    arr = list(map(int, input().rstrip().split())
    
    miniMaxSum(arr)
```