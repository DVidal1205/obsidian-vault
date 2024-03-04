### Binary
Multiplication
- 1100 x 1110
- Take each of the right digits and multiply by the other
- 1100 * (1000 + 100 + 10 + 0)
- Distribute appropriately
- 10101000
Subtraction
- Simply add together a plus the negative complement
- 10 - 126 = 10 + (-126)
- 10: 00001010
- -126: 10000010
- 10 - 126: 10001100
### Representing negative numbers
Twos complement!!!
- A binary string of length n can represent a number $-2^{n-1} \le i \le 2^{n-1}$
- The highest order bit position (#n-1) represents a coefficient multiplying by -2^(n-1)
- If the leading number is 1, throw a negative in front of the complement number + 1
- 11111111 = -( (00000000) + 1) = -1
- 10000001 = -( (01111110) + 1 ) = 127
