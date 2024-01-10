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
- 

$p \leftrightarrow q \leftrightarrow (p \to q) \land (q \to p)$
