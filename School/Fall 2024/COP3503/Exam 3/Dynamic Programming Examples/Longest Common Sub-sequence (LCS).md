# LCS
Most applicable in bioinformatics and genetics. A sub-sequence are letters that do not have to be adjacent, just in that order.
- A**C**CG**GT**
- GT**CGT**T
- Sub-sequence CGT with a value of 3

Given a sequence X = <X1, X2, X3, ... , Xm> and a sequence Z = <Z1, Z2, Z3, ... , Zk> we can say a sub-sequence exists if there is a strictly increasing sequence I = <I1, I2, I3, ... , Ik>.

## Recursive Approach
We can represent each problem as a pointer to a specific index in the string. We initialize both of them at positions m and n, which are the end of the string.
1. Either are 0, then we return 0 as the base case
2. If the pointers point to the same value, return 1 + the call of BOTH previous
3. If they are not the same, find the max and return
```java
int LCS(String X, String Y, int m, int n){
	// Base Case
	if (m == 0 || n == 0){
		return 0;
	}

	// Case where they are the same
	if (X.chartAt(m-1) == Y.charAt(n-1)) {
		return 1 + LCS(X, Y, m-1, n-1);
	}

	// Case where they are different
	return max(LCS(X, Y, m-1, n), LCS(X, Y, m, n-1));
}
```
## Memoization Approach
Same thing as the Recursive Approach, just apply the cache/memo.
```java
int LCSMemo(String X, String Y, int m, int n, int[][] memo){
	// Base Case
	if (m == 0 || n == 0){
		return 0;
	}

	// In memo
	if (memo[m][n]] != -1){
		return memo[m][n];
	}

	// Case where they are the same
	if (X.chartAt(m-1) == Y.charAt(n-1)) {
		memo[m][n] = 1 + LCSMemo(X, Y, m-1, n-1);
		return memo[m][n];
	}

	// Case where they are different
	memo[m][n] = max(LCSMemo(X, Y, m-1, n, memo), LCSMemo(X, Y, m, n-1, memo));
	return memo[m][n];
}
```