### Card Combinatorics
$\frac{13 * C(4, 2)}{C(52, 2)}$
- There are 13 suits of cards, and there are 4 of each card. We only need 2, hence the C(4,2)
- In the denominator is our number of possible experiments, which is of 52 cards picking two, hence the C(52, 2)
- C notation means $C(x, y) = \frac{x *x-1}{y}$

### Logical Operators
Logical Or - $\lor$
- p $\lor$ q is true when either p or q are true, inclusive of the case where both are true
Logical And - $\land$
- p $\land$ q is true when both p and q are true
Logical Exclusive Or - $\oplus$
- p $\oplus$ q is true either p or q are true, but not both

### Implication Conditional
Implication - $\rightarrow$
- p $\rightarrow$ q is true when q is true when p is true, but not vise versa
- p is a sufficient condition for q
- q is a necessary condition for p 
- if p is false, then no matter what the conclusion is, the implication holds

#### Other Conditionals for p implies q
**Converse:** $q \rightarrow p$
**Contrapositive:** $\lnot q \rightarrow \lnot p$ (Always the same truth value as the original implication)
**Inverse:** $\lnot p \rightarrow \lnot q$
(Converse and Inverse are always the same truth value as each other, since the Inverse is technically the Contrapositive of the Converse)
#### Truth Tables
| p   | q   | p $\rightarrow$ q | q $\rightarrow$ p | $\lnot q \rightarrow \lnot p$ | $\lnot p \rightarrow \lnot q$ |
| --- | --- | ----------------- | ----------------- | ----------------------------- | ----------------------------- |
| 0   | 0   | 1                 | 1                 | 1                             | 1                             |
| 0   | 1   | 1                 | 0                 | 1                             | 1                             |
| 1   | 1    | 1                  | 1                  | 1                              | 1                              |
| 1    | 0    | 0                  | 1                  | 0                              | 1                              |

### Biconditional Connective
- p$\leftrightarrow$q
- True when both have the same truth value
- Equivalent to (p$\rightarrow$q)$\land$(q$\rightarrow$p)
- p is a necessary and sufficient condition for q
- if p then q, and conversely
- p iff q
- x>0 if and only if x^2 is positive

### Truth Table 
| p | q | p $\land$ q | q $\lor$ p | $q \oplus p$ | $p \rightarrow q$ | $p \leftrightarrow q$ |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 | 1 |
You need 2^n rows for the number of propositions  you have

### Construct
( (p $\land$ q) $\lor$ $\lnot$q)

| p   | q   | (p $\land$ q) | $\lnot q$ | ( (p $\land$ q) $\lor$ $\lnot$q) |
| --- | --- | ------------- | --------- | -------------------------------- |
| 0   | 0   | 0             | 1          | 1                                 |
| 0   | 1   | 0              | 0          | 0                                 |
| 1   | 0   | 0              | 1          | 1                                 |
| 1   | 1   | 1              | 0          | 1                                 |

### Order of Operations
1. Negation ($\neg$)
2. Conjunction ($\land$)
3. Disjunction ($\lor$)
4. Exclusive Or ($\oplus$)
5. Implication ($\rightarrow$)
6. Biconditional ($\leftrightarrow$)

### Propositional Equivalnces
- A compound proposition that is always true, no matter the truth values of the propositions, is a tautology
- A compound that is always false is a contradiction
- Tautology: $p \lor \lnot p$
- Contradiction: $p \land \lnot p$
- Conditions are logically equivalent if p $\leftrightarrow$ q is a tautology

### Arithmetic
a + b = b + a
(a + b) + c = a + (b + c)
a*(b + c) = a * b + a * c

### Equivalence Laws
Identity:
- $p \land T \leftrightarrow p$
- $p \lor F \leftrightarrow p$
Domination
- $p \lor T \leftrightarrow T$
- $p \land F \leftrightarrow F$
Idempotent
- $p \lor p \leftrightarrow p$
- $p \land p \leftrightarrow p$
Double Negation
- $\lnot \lnot p \leftrightarrow p$
Commutative:
- $p \lor q \leftrightarrow q \lor p$
- $p \land q \leftrightarrow q \land p$
Associative:
- $(p \lor q) \lor r \leftrightarrow p \lor (q \lor r)$
- $(p \land q) \land r \leftrightarrow p \land (q \land r)$
Distributive:
- $p \land (q \lor r) \leftrightarrow (p \land q) \lor (p \land r)$
- $p \lor (q \land r) \leftrightarrow (p \lor q) \land (p \lor r)$
De Morgan's:
- $\lnot (p \land q)  \leftrightarrow (\lnot p)  \lor (\lnot q)$
- $\lnot (p \lor q)  \leftrightarrow (\lnot p)  \land (\lnot q)$
Negation:
- $p\lor\lnot p\leftrightarrow T$
- $p\land\lnot p\leftrightarrow F$
Exclusive or Equivalence:
- $p \oplus q \leftrightarrow (p \lor q) \land \lnot (p \land q)$
- $p \oplus q \leftrightarrow (p \land \lnot q) \lor  (q \land \lnot p)$
Implies:
- $p \to q \leftrightarrow \lnot p \lor q$
Biconditional (2 statements):
- $p \leftrightarrow q \leftrightarrow (p \to q) \land (q \to p)$

### Propositional Satisfiability
- A compound proposition is satisfiable if there is an assignment of truth values to its variables to make it true
### Predicate Logic
- Distinguishes subject from predicate
- **The dog is sleeping**
- Subject: dog
- Predicate: is sleeping
### More Predicates
- Convention: lowercase variables x, y, z denote objects
- Uppercase variables, P, Q, R denote propositional functions (predicates)
- Predicate P = "is sleeping"
### Universes of Discourse
- Define all the objects
- The collection of values that an object variable x can take
- x: professor
- y: students
- z: grades
### Quantifiers
- Quantify how many objects in the universe of discourse satisfy a given predicate
- How many P(x) are true?
### For All (Universal Quantifier)
- $\forall$ is the FOR all or universal quantifier means for all x in the domain that P holds
- Let the universe be real numbers
- Let $P(x) = \frac{x}{2} < x$
	- is $\forall x P(x)$  true?
	- Not true for -4
	- If the universe is all positive numbers, then the predicate holds
- Only need to find one exception to disprove a universal quantification
### Exists (Existential Quantifier)
- Let the u.d. of x be the Seats in a classroom
- Let P(x) be the predicate "x is occupied"
- Seats in a classroom
	- "Some of the seats are occupied"
	- "At least one seat is occupied"
- To show an existential quantification is true, you only have to find one value to prove it
- To show it is false, you must prove it is false for ALL values
### Binding Variables
- When a quantifier is used on a variable x, we say that x is bound
- If no quantifier is used on a variable, the variable is free
### Inference
- Methods of Mathematical Argument can be formalized in terms of rules of logical inference
- p = "you are in the class"
- $p \rightarrow q$ = "if you are in class, then you get a grade"
- What is q? (You will get a grade)
- q is the conclusion, and the first two statements are premises
- $\therefore$ q 
### Modus Ponens
- Consider $(p \land (p \rightarrow q)) \rightarrow q$
- Premises: $p$ and $p \rightarrow q$
- $\therefore q$
### Some Inference Rules
p, therefore p or q - Addition
p and q, therefore p or therefore q - Simplification
p q, therefore p and q

### Inference Rules of Quantifiers
Universal Instantiation
$\forall x P(x) \therefore P(c)$
Existential Instantiation
$\exists xP(x) \therefore P(c)$ for some $c$
Universal Generalization
$P(c)$ for all c $\therefore \forall x P(x)$
Universal Generalization
$P(c)$ for some c $\therefore \exists x P(x)$

### Proof Methods
#### Direct Proof
- Prove the statement ($p \rightarrow q$)
#### Indirect Proof
- Prove the contrapositive ($\lnot q \rightarrow \lnot p$)
#### Proof by Contradiction
- Sow that $\lnot q$ and $p$ cannot be true at the same time, proving q must be true
#### Vacuous Proof
#### Trivial Proof
#### Proof by Cases
- Cover all possibilities