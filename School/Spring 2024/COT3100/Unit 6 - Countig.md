## Permutations
P(n, r) = n! / (n-r)!
## Combinations
C(n,r) = P(n,r)/P(r,r) = n!/r!(n-r)!
## Cash Box Example
- The cash box can be arranged as bars and stars, where bar is a separator and the stars are dollars
- * * | | | | | | ***
- 11 items (5 bills + 6 bars)
- Since order matters with 11 positions
- C(11, 6) = C(11, 5)
- Now n = 7, r = 5
- C(n-1+r, r)
## Equations
r-p without repetition: n!/(n-r)!
r-p with repetition: n^r
r-c without repetition n!/r!(n-r)!
r-c with repetition: (n + r - 1)! / r!(n-r)! - C(n + r - 1, r)

## Discrete Statistics
Laplace's Definition
- Example: An urn contains four blue balls and five red balls. What is  the probability that a ball chosen from the urn is blue
- 4/9
- Example: What is the probability that when two dice are rolled the sum of the numbers on the dice is 7
- 1+6, 6+1, 2+5, 5+2, 3+4, 4+3
- 6/36