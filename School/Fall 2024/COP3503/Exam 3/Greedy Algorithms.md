## What is a Greedy Algorithm?
In all honesty, a greedy algorithm is really just brute force, minus the brute. Think about the problem, find a clever assumption based on the problem statement, and then abuse it. Greedy algorithms assume the best case at the **current moment** and solves the global problem, not the sub problem.
### Coin Change
Given a number of coins, `n`, return the **minimal** number of coins that can be given as change for that coin.
- **Greedy Assumption:** use math and grab the largest coins as change first, working down the hierarchy.
```java
public int MakeChangeGreedy(int n){
	quarters = n/25;
	k = n % 25;

	dimes = k / 10;
	k = k % 10;

	nickels = k / 5;
	k = k % 5;

	pennies = k;

	return (quarters + dimes + nickels + pennies);
}
```

### Fractional Knapsack
A thief robbing a store finds n items, where the *ith* item costs *vi* dollars and weighs *wi* pounds. Find the maximum profit the thief can leave with, given they can only carry a weight of W in the knapsack.
- **Greedy Assumption:** sort all of the items by their fractional value (v/w) and then grab as much of the front item as possible until the knapsack fills.
```java
public int FractionalKnapsack(int weight, int n){
	// Create the starting array and load with 0
	arr I[] = sorted(I) // By v/w
	for (int i = 1; i < n; i++){
		I[i] = 0;
	}

	// Loop
	int load = 0;
	int value = 0;
	i = 1
	while (load < weight && i <= n) {
		if (weights[i] < weight - load) {
			I[i] = 1
		} else {
			I[i] = (weight - load) / weights[i]
		}
		load = load + I[i] * weights[i];
		value = value I[i] * values[i];
		i = i + 1
	} 
	return value;
}
```