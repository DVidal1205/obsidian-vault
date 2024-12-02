## Dijkstra's Algorithm - One to All (no Negatives) 
Dijkstra's Algorithm finds the shortest path distance from one source node to all other nodes in the graph, and **does not contain negative edges.** This is because once a path is visited, it is assumed there is no quicker path, which negative edges contradict. O(E + V log V)
- Create a priority queue and insert the source, and all of its edges with their distances
- Travel to the vertex with the smallest weight, and mark it as visited (no more updates)
- **Relax** the distances with the new found edges
	- **Relaxing** an edge means decreasing its distance from the source with the newfound cost from traveling over a node
- Travel and traverse over all nodes until all edges are relaxed and all nodes are visited.
## Floyd Warshall's - All to All (with Negatives)
Bellman Fords also finds the shortest path distance from all nodes to all other nodes, **but it can contain negative edges.** This uses a 2-D array and a runs an iteration over the graph for updates. It allows for negative edges by doing intermediate testing from ALL to ALL. Note, a negative cycle would also result in an infinite loop. O(V^3) where V is the number of edges.
- Initialize an N x N adjacency matrix where N is the number of nodes
- Initialize all of the paths that are currently present by indexing into the matrix (If node 1 connects to node 4 with a weight of 5, then adj[1,4] = 5). Set all other values to infinity.
- Initialize 3 looping variables up to N, i j and k.
	- If the distance from adj[i, j] is greater than dist[i, k] + dist [k, j] then update adj[i, j] to that.
	- This works, because it is checking if there is a quicker path by using an **intermediate** vertex.
## Bellman Ford's - One to All (with Negatives)
Bellman Ford operates on a fundamental idea, that there is at most |v| - 1 edges in the shortest path. If it is more than that, there must be a cycle. There are multiple iterations of Bellman Ford's. Runtime of O(|V| * |E|)
- Make a tabulation table with the source node at index 0 with a distance of 0, and all others with the distance of infinity.
- Update the table with all of the edges based on the new node. Skip if we cannot traverse.
	- If distance of current + weight from current to source is less than the distance of the source, **relax** the weight
- Loop again, since we now have all of our discovered nodes and edges. Negative edges are now discovered and we can apply negative edges.
- Loop until all of the values remain the same
# Dijkstra's vs Bellman Ford's
Dijkstra's only traverses once so it is quicker, but cannot support negative weights. Bellman-Ford does the same type of approach, but instead of using a priority queue enforces DP by iterating over all elements and updating in multiple loops.
