### Supermarket Basket Analysis
- Which items are frequently purchased together by customers
- Given a set of transactions, find rules that will predict the occurrence of an item with other items
### Apriori Algorithm
- Frequency of a larger set is less than a smaller set that is a part of the larger set.
### Set Theory
- Founded by George Cantor
- Set is a new type of structure, representing an unordered collection of zero or more distinct objects
- Sets are ubiquitous in computer science for database querying, programming, and data mining
### Set Notation
- Denoted by (S, T, U)
- Listing all of its elements in curly braces: {1, 2, 3, 4}, {a, b, c}
- Set Building Notation: {x|P(x)}, which means all elements that satisfy P(x) are in the domain of the set
- If P(x) is x>0 or x<6, then Set P = {1, 2, 3, 4, 5}
- $x\in S$ means x is in S
- $x \notin S$ means x is not in S, also $\lnot (x\in S)$
- Sets can contain infinitely any numbers
### Common Sets
- N - Natural - {0, 1, 2, 3...}
- Z = Zntegers = {..., -2, -1, 0, 1, 2...}
- R = Real Numbers
- $\varnothing$ = "null", or the "empty set"
	- $\varnothing$ = {}
### Subset and Superset Relations
- $S \subseteq T$ means S is a subset of T, and it is contained within T
- $T \supseteq S$ means T is a superset of S, and S is contained within T
- $\varnothing \subseteq S$, and $S \subseteq S$.
### Strict Subset
$S \subset T$ means S is a proper subset of T, meaning that $S \subseteq T$, but $\lnot (T \subseteq S)$
### The Power Set
- The power set, P(S) of a set S is the set of all subsets of S
- $P(S) = x|x\subseteq S$
- P({a,b}) = {$\varnothing$, {a}, {b}, {a,b}}