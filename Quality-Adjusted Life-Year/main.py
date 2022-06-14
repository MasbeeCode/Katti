# The Quality-Adjusted Life-Year (QALY) is a way to measure a person’s quality of life that includes both the quality and the quantity of life lived.

# The quality of life lived can be quantified as a number between 0 and 1. 
# If someone is living with perfect health, the quality of life is 1. If someone is dead, then the quality of life is 0. 
# The quality of life may increase or decrease due to medical treatements, sickness, etc.

# The QALY for each period in which the quality of life is constant is simply the product of the quality of life and the length of the period (in years). 
# We wish to know the amount of QALY accumulated by a person at the time of death, given the complete history of this person.

# Get number of iterations
n = int(input())

total = 0

# Get value pairings, multiple them, then increase total
for i in range(n):
    vals = input().split(" ")

    total += float(vals[0]) * float(vals[1])

# Return result
print(total)
