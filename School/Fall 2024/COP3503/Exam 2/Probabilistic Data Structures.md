## Treap
- Heap: array that can be seen as a newly complete binary tree where the keys must satisfy the heap (max and min)
- Tree + Heap = Treap
- Almost balanced binary tree
### Treap Insertion
- Perform BST insertion
- Randomly assign a priority
- Fix heap priority based on assigned property
### Treap Deletion
- Just set the priority to zero. It will rotate and rebalance until it is a leaf, and then delete.