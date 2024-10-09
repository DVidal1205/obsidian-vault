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

### Deletion
- Predecessor and Successor
- Reach the key, traverse from the root to the key
#### Scenarios/Rules
1. If the key k is a part of a leaf node, then just delete the key
2. Not a leaf, and the key is an internal node
	1. Look left, and can we bring up a predecessor from a LEAF node with t keys
	2. If that doesn't work, look right for a successor and do the same.
	3. If that doesn't work, merge the desired key DOWN into its children, creating a full leaf node, and delete the key
3. 