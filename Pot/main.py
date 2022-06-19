x = int(input())

# Read inputs and calc total. Read last index, then pow the number excluding the last digit
total = 0
for i in range(x):
    y = input()
    total += pow(int(y[:len(y) - 1]), int(y[len(y) - 1]))

# Output
print(total)