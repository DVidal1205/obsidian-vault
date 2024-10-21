Dynamic programming is a technique, and not a set algorithm.
- Dynamic programming is applicable when the sub problems are *not* independent.
## Steps to developing a DP solution
1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a top-down (memoization) or bottom-up (tabulation) fashion
## Memoization vs Tabulation
Memoization
- Top-Down
- Recursive
- Utilize subproblems that have overlap
Tabulation
- Bottom-Up
- Iterative
- Utilize subproblems that DONT have overlap