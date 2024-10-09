## What is a RBT
- A specialized Binary Search Tree that keeps things balanced
- Nodes:
	- color
	- key
	- left
	- right
	- parent
## Properties
- Every node is either red or black
- The root is black
- Every leaf is black
- If a node is red, then both the children are black
- For each node, all simple paths from the node to descendant leaves contains the same number of black nodes.
- All new nodes are inserted as red
## AVL vs RBT
- Searching a RBT is hard, but insertion and deletion are quick.
- AVL's are better for searching
## Insertion
