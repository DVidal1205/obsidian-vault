# Notations
1. Big Oh 
2. Big Theta
3. Big Omega
4. Little Oh
5. Little Omega

## Big Oh
- Gives an upper bound on a function within a constant factor
- Informal definition was dropping the coefficient and keeping the largest growth factor
#### Problem
Show that $3n^{2}-6$ is bound by $O(n^4)$
- Find that $0 \leq T(n) \leq cf(n)$
- $0 \leq 3n^{2}-6 \leq cn^4$
##### LHS
- $0 \leq 3n^{2}-6$
- $6 \leq 3n^{2}$
- $2 \leq n^{2}$
- $\sqrt{2} \leq n$
##### RHS
- $3n^{2}-6 \leq cn^4$
- $0 \leq cn^{4}- 3n^{2}+6$
	- pick any value of C greater than input
- $0 \leq n^{2}(n^{2}-3)+6$
- Check if each term is greater
	- $0 \leq 6$ YES
	- $0\leq n^{2}$ YES, n > 1
	- $0 \leq n^{2}-3$ YES

## Big Omega
Used to give a lower bound on a function within a constant factor
Find that $0 \leq cf(n) \leq T(n)$
Show that $3n^{2}+2$ = $\Omega (n)$
##### LHS
- $0 \leq cn$
- Always satisfactory
##### RHS
- $cn \leq 3n^{2}+2$
- $0 \leq 3n^{2}-cn+2$ (let c=3)
- $0 \leq 3n^{2}-3n+2$
- $0 \leq 3n(n-1)+2$
## Big Theta
Used to give a bound on a function within a constant function
$0 \leq c_{1}f(n) \leq T(n) \leq c_{2}f(n)$

Show that 8n^2 - 6n + 3 = $\theta (n^2)$
## Assessing Existence
Before working on proving a solution, first prove that it exists. Consider f(n) the function and g(n) the bound function ($n^2$ in the case of $O(n^2)$).
1. $T(n) = O(f(n))$ if $f(n) \leq g(n)$
1. $T(n) = \Omega(f(n))$ if $f(n) \geq g(n)$
1. $T(n) = \Theta(f(n))$ if $f(n) = g(n)$
## Master's Theorem
An approach to solving recurrence relations in the form: $T(n) = aT(\frac{n}{b}) + f(n)$
### Three Cases of Master's Theorem
Case 1: $f(n) = O(n^{log_{n}- \epsilon})$, $\epsilon > 0 \geq T(n) = \theta(n^{log_n})$
Case 2: $f(n) = \theta(n^{log_{n}})$, $T(n) = \theta(n^{log_n}log_n)$
Case 3: $f(n) = \Omega(n^{log_{n} + \epsilon})$, $\epsilon > 0 \geq T(n) = \theta(f(n))$
![[Asymptotic Notations 2024-08-26 17.02.07.excalidraw]]

## Lab
![[Asymptotic Notations 2024-08-30 14.31.44.excalidraw]]


1. $3n^{2}-100n+6 = O(n^{2})$ (TRUE, since the degrees are equal and O must be greater or equal)
1. $3n^{2}-100n+6 = \theta(n^{4})$ (FALSE, since the degrees are equal and $\theta$ must be equal)
1. $2^{(n+1)} = \theta(2^{n})$ (TRUE, since the degrees are equal and $\theta$ must be equal)