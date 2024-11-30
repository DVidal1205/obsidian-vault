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
		memo[m][n] = 1 + LCSMemo(X, Y, m-1, n-1, memo);
		return memo[m][n];
	}

	// Case where they are different
	memo[m][n] = max(LCSMemo(X, Y, m-1, n, memo), LCSMemo(X, Y, m, n-1, memo));
	return memo[m][n];
}
```
## Tabulation Approach
Build the table Bottom-Up and solve similar to memoization approach. Initialize the top and left row to 0.
- Index i and j represent the position of the pointer on the string, m and n. For example, c(5, 7) means index 5 of String X and index 7 of String Y.
- If they are different, pull the max value from either the above cell or left cell (take the answer from that sub problem.)
- If there is a match, take diagonal and add 1 to it
```java
int LCSTabulation(String X, String Y, int m, int n) {
	int c[][] = new [m+1][n+1] // Numerical Solution
	char r[][] = new char[m+1][n+1] // String Solution

	// Initialize Top and Left row to zeroes 
	for (int i = 0; i <= m; i++){
		c[i][0] = 0;
	}
	for (int j = 0; j <= n; j++){
		c[0][j] = 0;
	}

	// Build the table
	for (int i = 1; i <= m; i++){
		for (int j = 1; j <= n; j++){
			if (X.charAt(i-1) == Y.charAt(j-1)) {
				c[i][j] = 1 + c[i-1][j-1] // Take Diagonal
				r[i][j] = 'd';
			} else if (c[i-1][j] >= c[i][j-1]) // Choose Up
				c[i][j] = c[i-1][j];
				r[i][j] = 'v';
			} else {
				c[i][j] = c[i][j-1];
				r[i][j] = 'h';
			}
		}
	}
	return c[i][j];
}
```