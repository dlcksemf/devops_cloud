import random

total = 100000
ev = 0

for number in range(total):
    x = random.random()
    y = random.random()

    if x * x + y * y <= 1.0:
        ev += 1

print((ev / total) * 4)
