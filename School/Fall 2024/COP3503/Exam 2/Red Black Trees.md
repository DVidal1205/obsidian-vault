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
## AVL vs RBT
- Searching a RBT is hard, but insertion and deletion are quick.
- AVL's are better for searching
## Rotations
### Left Rotation
![[Pasted image 20241011135201.png]]
### Right Rotation
![[Pasted image 20241011135217.png]]


## Insertion
1. Insert Z and color it red
2. Fix violations

- Create a red node with NIL pointers.
- Perform BST insertion, and color it red on insertion.

0. Z = root
	- Insert and color Z black
1. Z uncle = Red
	- Invert color of parent, grandparent, and uncle
1. Z uncle = black (triangle)
	- Z, parent, and grandparent form a triangle
![[Pasted image 20241011135717.png]]

- Rotate the parent, doing so in the opposite direction of Z so Z takes the place of the parent
1. Z uncle = black (line)
![[Pasted image 20241011135846.png]]
	- Rotate Z's grandparent away from Z, so its parent becomes the grandparent
	- Recolor original parent and grandparent
![[Pasted image 20241011140016.png]]



## Deletion
X is the node deleted, and W is the sibling of X

Case 1: X's Sibling W is red.
- Change sibling to black
- Change parent to red
- Rotate towards the deleted node
- Reassign W to the new sibling

Case 2: X's Sibling W is black AND both of W's children are black
- Change sibling to red
- Set X to parent 

Case 3: X's sibling W is black, W's left child is red and W's right child is black
- Recolor the left red node to black
- Recolor W to red
- Rotate right at W (away from former red child)

Case 4: X's sibling W is black, W's right child is red and W's left child is black
- Recolor W to X's parent color
- Color X's Parent to Black
- Color W's right child to black
- Rotate the parent towards X