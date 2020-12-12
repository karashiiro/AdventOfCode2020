import itertools
import math

TARGET_YEAR = 2020

# Load inputs
with open("input.txt", "r") as file:
    input_txt = str(file.read())
    inputs = [int(line) for line in input_txt.split("\n")]

# Narrow search space
minimum = min(inputs)
trimmed_inputs = [input for input in inputs if input + minimum <= TARGET_YEAR]
trimmed_inputs.sort()
trimmed_inputs = list(itertools.dropwhile(lambda x: x  + trimmed_inputs[len(trimmed_inputs) - 1] < TARGET_YEAR, trimmed_inputs))
print(trimmed_inputs)

# Search the remainder
for combo in itertools.combinations(trimmed_inputs, r=3):
    if sum(combo) == TARGET_YEAR:
        print("Solution entries: %d, %d, %d" %combo)
        print("Solution: %d" %math.prod(combo))
        break

