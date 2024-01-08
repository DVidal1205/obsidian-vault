# Chapter 3 - Probability
## Section 3.1 - Events, Sample Spaces, and Probability
- **Experiment:** an act or process of observation that leads to a single outcome that cannot be predicted with certainty
- **Sample Point:** the most basic outcome of an experiment
	- Ex: Heads or Tails in a Coin Flip Experiment (S: {H, T})
	- Ex: 1 through 6 in a d6 Experiment (S: {1, 2, 3, 4, 5, 6})
- **Sample Space:** the collection of all of an experiment's sample points
- **Tree Diagram:** A way of depicting all of the outcomes for an experiment, with the bottom nodes being all possible combinations for the sample space
![[Pasted image 20230911143909.png]]
- **The Law of Large Numbers:** the law states that the relative frequency of the number of times that an outcome occurs when an experiment is replicated over and over again approaches the true probability of the outcome
- **Probability Rules for Sample Points:**
	- Let $p_{i}$ represent the probability of a sample point $i$ 
		- All sample point probabilities *must* lie between 0 and 1 (i.e. $0 \le p_{i} \le 1$)
		- The probabilities of all the sample points within a space *must* sum to 1 (i.e. $\sum p_{i} = 1$)
- **Event:** a specific collection of sample points
![[Pasted image 20230911145037.png]]
## Section 3.2 - Unions and Intersections
Compound Events
- **Union:** the event that occurs if either A or B or both occur on a single performance of the experiment: $A \cup B$
- **Intersection:** the event that occurs if both A and B occur on a single performance of the experiment: $A \cap B$
## Section 3.3 - Complementary Events
- **Complement:** the event that A does *not* occur - the event consisting of all sample points that are not event A: $A^C$ 
	- Rule of Complements: $P(A) + P(A^{C)}= 1$
## Section 3.4 - Additive Rule and Mutually Exclusive Events
- **Additive Rule of Probability:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Mutually Exclusive:** if $A \cap B$ contains no sample points
	- Probability of Union of Mutually Exclusive Events = $P(A \cup B) = P(A) + P(B)$
## Section 3.5 - Conditional Probability
- **Unconditional Probabilities:** no special conditions are assumed other than those that define the experiment
- **Conditional Probability:** opposite of unconditional probabilities: 
- **Conditional Probability Formula:** $P(A|B) = \frac{P(A\cap B)}{P(B)}$
## Section 3.6 - The Multiplicative Rule and Independent Events
- **Multiplicative Rule of Probability:** $P(A\cap B) = P(A)P(B|A)$, $P(A\cap B)=P(B)P(A|B)$
- **Independent Events:** do not alter the probability of the other occurring
	- $P(A|B) = P(A)$
	- $P(B|A) = P(B)$
![[Pasted image 20230918150939.png]]

|                      | Under 55 | 55 and Older | Total |
| -------------------- | -------- | ------------ | ----- |
| Can't Afford Insulin | 68       | 83           | 149   |
| Can Afford Insulin   | 76       | 62           | 138   |
| Total                | 142      | 145          | 287      |
