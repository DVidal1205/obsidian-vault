A data structure that neatly stores overlaps
- Sets are represented by their representative root node, which all of the others in the set point to.
- Path shortening optimizations are used to make all elements in a set point directly to the representative
	- Can be done in insertion or traversal, different costs for both
- Sets are merged by making the representative of a set a child of the representative of another set
	- Can be optimized by rank union - making the smaller union the child
Can be represented via Linked Lists, or an array of sets that represent trees