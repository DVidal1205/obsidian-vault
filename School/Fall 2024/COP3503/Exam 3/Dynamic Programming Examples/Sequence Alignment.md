Example: Google Search Alignment
"Did you mean: bibliography?"
# The Problem
Given two sequences with possibly differing sizes, make them match as closely as possible.
- A match is a set of ordered pairs with the property that each item occurs in at most one pair.
- A matching M of these two sets is an alignment if there are no crossing pairs.
![[Pasted image 20241129191401.png]]
- We may also want to look at the gap penalty for typos, or how far the two letters are on the keyboard alpha