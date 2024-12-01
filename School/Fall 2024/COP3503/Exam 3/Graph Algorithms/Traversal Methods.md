## Breadth First Search (BFS)
Breadth First search takes a source node and iterates over the graph in the following algorithm.
1. Create a queue and initialize it with the source node with a depth of 0
2. Enqueue all of its edges into the queue with a depth of 1
3. While the queue still exists, dequeue the front and enqueue all of the adjacent edges with a depth of depth + 1
### Breadth Search Tree
- The initial graph, only containing the edges used in the breadth first search
## Depth First Search (DFS)
Depth First search does not take a source node and instead of iterating over neighbors, it will explore all the way down a certain path before returning. Keep a time variable globally. Each node will store a time of discovery/finish. Discovery represents the time stamp of when the node was found and the Finish represents when it is complete
1. Populate all of the vertexes as not visited with a predecessor of NIL. 
2. For each vertex, call the visit command
	1. Set the color to gray, and for each of its nodes, recursively visit that node if they are white
	2. Set the node to black as it recurses up and set the time to the proper time.
### Depth Search Tree
- The initial graph, only containing the edges used in the search. Can contain isolated nodes
### Topological Sort
- Nodes in a sorted order by time
