### Card Combinatorics
$\frac{13 * C(4, 2)}{C(52, 2)}$
- There are 13 suits of cards, and there are 4 of each card. We only need 2, hence the C(4,2)
- In the denominator is our number of possible experiments, which is of 52 cards picking two, hence the C(52, 2)
- C notation means $C(x, y) = \frac{x *x-1}{y}$

### Logical Operator
Logical Or - $\lor$
- p $\lor$ q is true when either p or q are true, inclusive of the case where both are true
Logical And - $\land$
- p $\land$ q is true when both p and q are true
Logical Exclusive Or - $\oplus$
- p $\oplus$ q is true either p or q are true, but not both
Implication - $\rightarrow$
- p $\rightarrow$ q is true when q is true when p is true, but not vise versa
- p is a sufficient condition for q
- q is a necessary condition for p 
- if p is false, then no matter what the conclusion is, the implication holds

### Other Conditionals for p implies q
**Converse:** $q \rightarrow p$
**Contrapositive:** $\lnot q \rightarrow \lnot p$
**Inverse:** $\lnot p \rightarrow \lnot q$

### Truth Tables
| p   | q   | p $\rightarrow$ q | q $\rightarrow$ p | $\lnot q \rightarrow \lnot p$ | $\lnot p \rightarrow \lnot q$ |
| --- | --- | ----------------- | ----------------- | ----------------------------- | ----------------------------- |
| 0   | 0   |                   |                   |                               |                               |
|     |     |                   |                   |                               |                               |

