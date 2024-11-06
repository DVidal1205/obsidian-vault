### What is a MST?
- Spanning tree - all edges are connected
- W(T) - minimum weight (edges)
### Kruskals (Queue)
- Sort all of the edges by weight
- Iterate over the edges
- Connect if not in disjoint set, else proceed
- Always gets the MST weight
### Primms (Priority Queue)
- Starts with a source node (difference from Kruskals)
- Create a map where all elements are in a priority queue with priority infinity and prev. of NULL
