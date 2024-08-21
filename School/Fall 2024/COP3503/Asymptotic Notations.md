# Notations
1. Big Oh 
2. Big Theta
3. Big Omega
4. Little Oh
5. Little Omega

### Big Oh
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
	- $0 \leq 6$
	- $\$