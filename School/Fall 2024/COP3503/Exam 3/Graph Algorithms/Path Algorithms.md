## One to All - Dijkstra's Algorithm
Dijkstra's Algorithm finds the shortest path distance from one source node to all other nodes in the graph, and **does not contain negative edges.** This is because once a path is visited, it is assumed there is no quicker path, which negative edges contradict.
- Create a priority queue and insert the source, and all of its edges with their distances
- Travel to the vertex with the smallest edge, and mark it as visited (no more updates)
- **Relax** the distances with the new found edges
	- **Relaxing** an edge means decreasing its distance from the source with the newfound cost from traveling over a node
- Travel and traverse over all nodes until all edges are relaxed and all nodes are visited.