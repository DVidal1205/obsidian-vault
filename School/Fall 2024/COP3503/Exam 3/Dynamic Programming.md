# Dynamic Programming
Dynamic programming is a technique, and not a set algorithm.
- Dynamic programming is applicable when the sub problems are *not* independent.
## Steps to developing a DP solution
1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a top-down (memoization) or bottom-up (tabulation) fashion
4. Construct the optimal solution from the result
## Memoization vs Tabulation
Memoization
- Top-Down
- Recursive
- Utilize sub-problems that have overlap
Tabulation
- Bottom-Up
- Iterative
- Utilize sub-problems that DON'T have overlap

# Case Study: Fibonacci 
## Pure Recursive
There is a lot of overlapping solution by using pure recursion in Fibonacci sequence. For exam
```java
int fib(int n) {
	if (n<=1){
		return n;
	} 

	return fib(n-1) + fib(n-2)
}
```