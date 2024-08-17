---
date: 2023-09-30
---
## Introduction
**Graphs** 
- Collection of vertices (nodes) and edges (arcs).
- The nodes represent a point of data
- The lines are edges
**Weighted Graphs** 
- Assign values to the edges (a cost related to connecting the two vertices together)
- Road or route weights could be the amount of time to travel there.
**Directed Graph (Digraph)**
- The edges on a directed graph can only be traveled across in one direction
**Connected Graph**
- A graph is connected if there is a path from every vertex to every other vertex (does not need a direct edge)
**Path**
- The list of vertices in which successive vertices are connected by edges
- A simple path is a path in which no vertex is repeated
	- A -> B -> D -> A -> C
	- A -> B -> D -> C
**Cycle**
- A simple path except that the first and last vertices are the same (it cycles)
	- 7 -> 5 -> 6 -> 8 -> 7
## Graph Representation
- Adjacency Matrix
- Adjacency List
- Edge List
- Adjacency Function
### Adjacency Matrix
- An N x N matrix where N is the number of vertices in the graph
- Can store boolean, is there an edge?
- Can store number (how many edges)
- Can store weights for weighted graph
### Adjacency List
- Store a list of neighbors for each node
## Algorithms
- Depth First Search
- Breadth First Search
- Topological Sort
- (Kruskal's Algorithm) Minimum Spanning Tree
- (Floyd Warshall's Algorithm) All-Pairs-Shortest Paths
- Two coloring
