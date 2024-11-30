Given an initial string s and a target string t, what is the minimum number of operations needed to turn s into t.
- Inserting a character
- Deleting a character
- Replacing a character
## Memoization
- If m is zero, return n. If n is zero, return m. This is because we need to perform those many delete operations to make them equal (different lengths)
- If they are the same, then traverse 1 backwards in both m and n
- If they are different, call all of the functions
	- Insert = s, t, m, n-1, memo
	- Replace = s, t, m -1, n-1, memo
	- Delete = s, t, m-1, n, memo
	- Return 1 + min(insert, replace, delete) (accrue one cost)
![[Pasted image 20241129211128.png]]
## Tabulation
Create a table where the top row is the target string, and the column is the source string. Space them with a space, and then set the top row to 0-n.
- If the letters are the same, grab diagonally
- If they are different, initialize with 1 + minimum from all directions
	- Left = removal