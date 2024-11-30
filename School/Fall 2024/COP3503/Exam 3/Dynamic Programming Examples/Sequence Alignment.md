Example: Google Search Alignment
"Did you mean: bibliography?"
# The Problem
Given two sequences with possibly differing sizes, make them match as closely as possible.
- A match is a set of ordered pairs with the property that each item occurs in at most one pair.
- A matching M of these two sets is an alignment if there are no crossing pairs.
![[Pasted image 20241129191401.png]]
- We may also want to look at the gap penalty for typos, or how far the two letters are on the keyboard alpha
- Delta: cost to insert a gap
- Alpha: the defined cost of a mis-match
The three main cases:
1. Pay the alpha and move to the next character over, alpha + OPT(m-1, n-1)
2. Not Aligned
	1. Pick a character from X, delta + OPT(m-1, n)
	2. Pick a character from Y, delta + OPT(m, n-1)
To Construct a Solution
- Go to corner cell
- Horizontal means an insertion of a gap in the X letter
- Vertical means an insertion of a gap in the Y letter
- Diagonal means both of the letters at that spot.

X: n _
Y: m e
## Tabulation Approach
1. Set table first row and column to 0, initialize each position by delta * i
2. Loop and assign A(i, j) = min(alpha + A[i-1, j-1], delta + A[i-1, j], delta + A[i, j-1])
3. return A[m,n]