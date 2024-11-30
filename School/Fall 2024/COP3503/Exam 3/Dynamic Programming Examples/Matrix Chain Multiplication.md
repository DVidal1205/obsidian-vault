Input: Sequence of n matrices <A1, A2, A3, ... , An>
Output: Desired multiplication setup where A1 * A2 * A3 * ... * An = ((A1 * A2) * (A3 * A4) * A5)
The chain means the matrices will be locked in their specific order
![[Pasted image 20241129200113.png]]
Note that a matrix of 5 x 4 crossed with 4 x 3 will result in 60 scalar multiplications (5 x 4 x 3). We want to minimize this cost