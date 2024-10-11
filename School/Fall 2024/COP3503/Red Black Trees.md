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
- The root is always black
- Every leaf is black and NIL
- If a node is red, then both the children are black
- For each node, all simple paths from the node to descendant leaves contains the same number of black nodes.
- All new nodes are inserted as red
## AVL vs RBT
- Searching a RBT is hard, but insertion and deletion are quick.
- AVL's are better for searching
## Insertion
- Create a red node with NIL pointers.
- Perform BST insertion, and color it red on insertion.
- CASE 1 (Z's Uncle Y is Red)
	- Change Z Parent and Uncle both to black
	- Change Z Grandparent to read
	- Recursively make the grandparent the Z node
- CASE 2 (Z's Uncle Y is Black and Z is a right child)
	- Perform a left rotation on Z's parent
- CASE 3 (Z's Uncle Y is Black and Z is a left child)
	- Change Z's parent to the color black
	- Change Z's grandparent to the color red
	- Perform a right rotation on Z's grandparent