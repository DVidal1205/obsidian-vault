## Single Source Shortest Path
- Multi-source is Floyd Warshall's
- **Input:** directed, weighted graph, and a sourve vertex
- **Output:** optimal path from the source to he destination
- **Assumption:** All input edges on the directed graph are non-negative
## Psuedocode
- Iterate over each vertex, and set distance to infinity and previous equal to none
- Set source to a distance of 0
- 