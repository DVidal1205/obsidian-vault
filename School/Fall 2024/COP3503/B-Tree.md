# B Tree degrees
- A degree *t* is used to determine the number of values in a node ranges from t-1 to 2t -1. Root is excluded from this rule. Always keep odd so there is a middle element and a choice is not needed. Only the leaves will be full due to "preparation splits"
## Operations
- Insert
- Delete
### Insertion
1. Perform a similar BST Insertion, starting at the root and working our way down.
	1. Reach a leaf node.
	2. May need to re-balance. 
		3. **Balancing Split Node**
		4. t=3, (1, 3, 5, 7, 9). We want to insert 10, so we split down 5.
		5. (1, 3) 5 (7, 9)
		6. The median node is promoted, with its left and right children being the new nodes
2. Insert the key at the leaf.