x = int(input())
y = int(input())
out = 0

if x > 0:
    if y > 0:
        out = 1
    else:
        out = 4
else:
    if y > 0:
        out = 2
    else:
        out = 3

print(out)