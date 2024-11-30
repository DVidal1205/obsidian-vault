Input: Sequence of n matrices <A1, A2, A3, ... , An>
Output: Desired multiplication setup where A1 * A2 * A3 * ... * An = ((A1 * A2) * (A3 * A4) * A5)
The chain means the matrices will be locked in their specific order
![[Pasted image 20241129200113.png]]
Note that a matrix of 5 x 4 crossed with 4 x 3 will result in 60 scalar multiplications (5 x 4 x 3). We want to minimize this cost
## Tabulation
Create two tables, M and S, and fill using bottom up approach. Both M and S should be N x N where N is the # of matrices
- Fill out M diagonals with 0
- Fill out each of the cells with their  2 multiplication costs in the M table, and mark S = 1 in the cell of the multiplication (A1 * A2, S[1,2] = 1)
- Fill out the costs of the N multiplication, where N > 2 as follows
	- Multiply a cell by an already computed bundle of N-1. Find the cost by doing Cost + Left * Bridge to Parenthesis * Right