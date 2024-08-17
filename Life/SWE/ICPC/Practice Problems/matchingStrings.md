---
date: 2023-08-14
platform: HackerRank
problem-name: matchingStrings
difficulty: Basic
success-rate: 97.22%
language: Python
solved: True
topic: interview-prep
---
# Problem Description
![[Pasted image 20230814150524.png]]
## First Impression
This seems hellish. Going to discussion board and dissecting their solutions.
## Solution Notes
- I had a feeling this would use the count module, but I was not quite sure how. Essentially, create a list for the resulting count, iterate through the queries, and append the count of each query in the strings. It looks something like this:
- `list_res.append(strings.count(i))` 
### Code Solution
```Python
import math
import os
import random
import re
import sys


def matchingStrings(strings, queries):

    list_res = []
    for i in queries:
        list_res.append(strings.count(i))
    return list_res

  
if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = [] 

    for _ in range(strings_count):

        strings_item = input()

        strings.append(strings_item) 

    queries_count = int(input().strip())
  
    queries = [] 

    for _ in range(queries_count):

        queries_item = input()

        queries.append(queries_item)
  
    res = matchingStrings(strings, queries)
  
    fptr.write('\n'.join(map(str, res)))

    fptr.write('\n')

    fptr.close()
```
