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
### Cartesian Products of Sets
- Create all possible combination of the elements in a number of sets
- For sets $A \times B$ = {(a,b) | $a\in A$ $\land$ $b\in B$}
- {a,b} $\times$ {1,2} = {(a, 1), (a,2), (b,1), (b,2)}
- Cardinality |A$\times$B| = |A||B|
### Union
- A $\cup$ B contains all elements in A or B
- {a, b, c}$\cup${2, 3} = {a, b, c, 2, 3}
### Intersection
- For Sets A, B, their intersection A$\cap$B is the set containing all elements that are in A and B
- {2, 4, 6}$\cap${3, 4, 5} = {4}
### Disjointedness
- Two sets A, B are called disjoint if A$\cap$B = $\varnothing$
### Inclusion-Exclusion Principle
- Given |A|, |B|, what is the cardinality of |A$\cup$B| and |A$\cap$B|
- |A$\cap$B| = |A| + |B| - |A$\cup$B|
- |A$\cup$B| = |A| + |B| - |A$\cap$B|
### Set Difference
- For sets A, B, the difference of A and B, written by A-B, is the set of all elements that are in A but not in B
### Set Complement
- All elements not in the other in the universe of discourse
### How to prove a set identity
- Truth tables
- Use membership Tables
- Use the basic set identity laws
- Prove each set is a subset of each other (Mutual Subset)
