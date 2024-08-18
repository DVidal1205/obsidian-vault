1. Summation and related exercises and more examples pdf
2. Algorithm Analysis 3 (Using summation for run-time/number of specific operations in a code)
3. Recurrence relation, derive recurrence relation from a code and run-time, related exercises, and more examples pdf
4. O(N^2) sorting algorithms, steps, exercises, codes, bug tracing, run-time analysis
5. Merge sort, steps, exercises, and codes, run-time analysis
6. Quick sort, steps, exercises, and codes, run-time analysis, in-place operation, comparison of quick sort and merge sort run-time, optimizing merge sort by using insertion sort, why quick sort is unstable (discussed in the lecture)?
7. Tree concepts, binary tree, and binary search tree as much as I can cover today.

![[Review 2024-03-27 15.38.46.excalidraw]]


# Summation
# Algorithm Analysis 3
# Recurrence Relations

T(n) = 2T(n/2) + 2, T(1) = 1
T(n) 4T(n/4) + 2 + 2
T(n) 8T(n/8) + 2 + 2 + 2

kth T(n) = 2^k T(n / 2^k) + 2k

n/2^k = 1
n = 2^k
log2n

2^k T(1) + 2k

2 ^ k + 2k

n + 2k
n + 2log2n

O(n)



T(n) = T(n + 2) + n, T(1) = 1

T(n) = T((n + 2) + 2) + n + n + 2

T(n) = T(n + 6) + n + n + 2 + n + 4


kth T(n) = T(n + 2k) + kn + 2k

n + 2k = 1
k = (1-n)/2

T(1) + kn
1 + kn
1 + n(1-n)/2
1 + n-n^2/2
O(n^2)



## Step 1: Iterate to find pattern
## Step 2: Express pattern in terms of kth iteration
## Step 3: Solve k = 1
## Step 4: Replace T(k) with T(1) and k with k in terms of n
## Step 5: Determine runtime
# Sorting
## N^2 Sorting Algorithms
## Merge Sort
## Quick Sort
## Insertion + Merge Sort
# Trees
## Traversal / Sort
## Height
## BST
## Perfect Tree
## Perfect BST
## BST Insertion
# Bit wise
## 10110101 10010110
## BETWEEN TWO
### AND (&) 
10110101
10010110
/////////////
10000100

01101010
0000001
0


merge step

1 3 5  6 8 / 2 4 7 9 10
10

1 2 3 5 67 8 9 



1 3 2 4

1 3 2 4

1 3 2 4

1 2 3 4


### OR (|) 
10110101
10010110
/////////////
10110111
### XOR (^)
10110101
10010110
/////////////
00100011


## BY ITSELF 10110101
### NOT (~)
- 01001010
### LEFT SHIFT (<<) - same as multiplying by 2^k
01001010 << 2
10010100
### RIGHT SHIFT (>>)
01001010 >> 1
00100101
## Applications

### LSB
01001011
AND
0000001

0000000






### All possible sequences of array with size n

```c
int n; // size
int target; // target
int i, j;
for (i = 0; i < (1 << n); i++){
	sum = 0;
	for (j = 0; j < n; j++){
		if (i & (1 << j) != 0){
			sum += array[j];
		}
	}

}




```

5 numbers
111111
00001
00010
00011
00100
00101
01100



00101
00001

1 arr[i] add to sum
00010
00100
01000
10000





10011
10010
10000
= 2


00101

00100

00001


5
00101 << 1
5 << 1
