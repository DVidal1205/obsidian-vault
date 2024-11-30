A spanning tree is a path on the graph that contains no cycles, aka only one edge between a node and the rest of the tree. A minimum spanning tree is one of the possible trees with the smallest weights.
## Kruskal's Algorithm
Kruskal's Algorithm is a **greedy** algorithm to construct a minimum spanning tree **without a source node**. The algorithm has a runtime of O(|E| log |E|) where n is the number of edges, and works as follows.
- Instantiate a disjoint set, and an array of edges sorted by their weight in increasing order
- Check if the smallest weighted edge is included in the spanning tree using disjoint set find method
	- If the edge is already in the tree, continue
	- If the edge is not in the tree, add it
## Prim's Algorithm
Prim's Algorithm is another **greedy** algorithm to construct a minimum spanning tree **with a specified source node**. This algorithm has a runtime of O(|E| log |V|) and works as follows.
- Create a priority queue of edges that contain the distance from the source, and the predecessor. Set all of the edges to infinite weight except the source, which is 0 and NIL
- Grab all of the adjacent edges to the MST and update their costs if they are lower. Iterate to the next in queue, aka the node with the smallest cost.
- Keep updating the costs until the priority queue is empty