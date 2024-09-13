Given an integer array, find all distinct combinations of a given length k, where the repetition of elements is allowed. Design a Backtracking solution. 

Let's say k=2 and the array contains 1,2, 1.
- 1, 1
- 1, 2
- 2, 2

Read in the numbers and pass to the following algorithm
1. Check if the output.size() == k, which is the base case, then return
2. Place the current number in the array
3. Increment and call function again
4. return and increment again