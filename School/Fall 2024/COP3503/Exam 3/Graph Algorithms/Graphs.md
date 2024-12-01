A graph is a set of vertices connected via a set of edges. A graph can be represented in two different ways.
## Adjacency Matrix
- A 2D array where the index represents a connection (1,4) means node 1 is connected to node 4
- In a directed graph, 1,4 and 4,1 may be different. In an undirected graph, insert 1 into both directions
- In an unweighted graph, indicate a connection with a 1. In a weighted graph, instead insert the weight
## Adjacency List
- An array of linked lists where the index is the source vertex, and each node in the linked list is a destination
- Better runtime but harder to implement
- Each source may also have a weight associated with it by making an Edge class