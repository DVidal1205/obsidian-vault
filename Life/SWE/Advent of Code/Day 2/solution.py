# Open the input.in file and read line by line into the reports
reports = []
with open("input.in") as f:
    line = f.readline()
    while line:
        report = [int(x) for x in line.split()]
        reports.append(report)
        line = f.readline()


# Function to determine if two levels are safe
def is_safe_levels(val1, val2, direction):
    difference = val2 - val1

    # Gatekeep a difference of 0
    if difference == 0:
        return False

    # Check for different direction as start
    if (difference > 0 and direction < 0) or (difference < 0 and direction > 0):
        return False

    # Check distances
    if abs(difference) > 3 or abs(difference) < 1:
        return False

    return True


def is_safe_report(report):
    n = len(report)

    # Prime the direction
    direction = report[1] - report[0]
    if direction == 0:
        return False

    # Iterate over all cells in report
    for i in range(n - 1):
        # Calculate the difference and check if it is safe
        if not is_safe_levels(report[i], report[i + 1], direction):
            return False

    return True


def is_safe_with_dampener(report):
    for i in range(0, len(report)):
        dampened = report[:i] + report[i + 1 :]
        if is_safe_report(dampened):
            return True
    return False


num_safe = 0
num_safe_dampened = 0
for report in reports:
    if is_safe_report(report):
        num_safe += 1
    elif is_safe_with_dampener(report):
        num_safe += 1
print(num_safe)
