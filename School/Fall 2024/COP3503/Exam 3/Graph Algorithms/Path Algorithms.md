## One to All (no Negatives) - Dijkstra's Algorithm
Dijkstra's Algorithm finds the shortest path distance from one source node to all other nodes in the graph, and **does not contain negative edges.** This is because once a path is visited, it is assumed there is no quicker path, which negative edges contradict.
- Create a priority queue and insert the source, and all of its edges with their distances
- Travel to the vertex with the smallest edge, and mark it as visited (no more updates)
- **Relax** the distances with the new found edges
	- **Relaxing** an edge means decreasing its distance from the source with the newfound cost from traveling over a node
- Travel and traverse over all nodes until all edges are relaxed and all nodes are visited.
## One to All (with Negatives) - Bellman-Ford
Bellman Fords also finds the shortest path distance from one source node to all other nodes, **but it can contain negative edges.** This uses a 2-D array and a runs an iteration over the graph for updates.
- Initialize an N x N adjacency matrix where N is the number of nodes
- Initialize all of the paths that are currently present by indexing into the matrix (If node 1 connects to node 4 with a weight of 5, then adj[1,4] = 5)
- Initialize 3 looping variables up to N, i j and k.
	- If the distance from adj[i, j] is greater than dist[i, k] + dist [k, j] then update adj[i, j] to that.
	- This works, because it is checking if there is a quicker path by using an **intermediate** vertex.