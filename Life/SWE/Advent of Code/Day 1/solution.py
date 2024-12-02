from collections import Counter

left = []
right = []

# Open the input.in file and read line by line
with open("input.in") as f:
    line = f.readline()
    while line:
        left_val, right_val = [int(x) for x in line.split()]
        left.append(left_val)
        right.append(right_val)
        line = f.readline()

# Sort the arrays
left = sorted(left)
right = sorted(right)


# Part 1, find difference
def find_distance(left, right):
    # Length check
    n = len(left)
    if n != len(right):
        return -1

    # Find the distance
    distance = 0
    for i in range(n):
        distance += abs(left[i] - right[i])

    return distance


print(find_distance(left, right))


# Part 2, assemble similarity scores
def find_similarity(left, right):
    # Create frequency map
    left_to_right = Counter(right)

    # Calculate similarity value
    similarity_value = 0
    for val in left:
        if val in left_to_right:
            similarity_value += val * left_to_right[val]
    return similarity_value


print(find_similarity(left, right))
