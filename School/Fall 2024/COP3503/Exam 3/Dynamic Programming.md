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
There is a lot of overlapping solution by using pure recursion in Fibonacci sequence. For example, in the case of Fib(10), it splits into Fib(9) and Fib(8), and Fib(9) will also recompute the value of Fib(8).
![[Pasted image 20241128215058.png]]

```java
int fib(int n) {
	// Base Case
	if (n<=1){
		return n;
	} 
	
	// Recursive Call 
	return fib(n-1) + fib(n-2)
}
```
## Memoization
The memoization solution works by creating a memo, also known as a cache. The cache will simply store answers to sub-problems, and then in other problems, we first check if this exists before proceeding.
**This is top down, since we are working towards the bottom of the tree and then recurse back up. **
```java
int fibWithMemo(int n, int memo[]) {
	int val;

	// Return the problem if we have seen it before
	if (memo[n] != -1) {
		return memo[n];
	}

	// Compute the value
	if (n == 1 || n == 2) {
		fibval = 1
	} else {
		fibval = fibWithMemo(n-1) + fibWithMemo(n-2);
	}

	// Update the Memo and return
	memo[n] = fibval;
	return memo[n]; 
}
```

## Tabulation
The tabulation solution works by creating a table. The table will store the result of the problem before it, creating the answer as we iterate.
**This is a bottom up solution since we are moving from the base of the problem and towards the solution.**
```java
int fibWithTable(int n){
	// Ensure we have n > 1
	if (n==1){
		return 1;
	}

	// Create table and populate the first two terms of fibonacci
	int [] table = new int[n + 1];
	table[0] = 0;
	table[1] = 1;

	// Build response
	for (int i = 2; i <= n; i++){
		table[i] = table[i-1] + table[i-2]
	}

	// Return Solution
	return table[n]
	
}
```
# Make Change with Provided Coins
Given a list of coins that we can use and a total amount of money we want to split, we want to use the fewest number of coins possible to sum up to that amount. Infinite quantity of each coins
- 
# Knapsack - All or Nothing, non-Fractional
The [[Greedy Algorithms]] approach to the Knapsack requires the ability to take a fractional item. In the case of all or nothing, we can use Dynamic Programming to accomplish this as well.