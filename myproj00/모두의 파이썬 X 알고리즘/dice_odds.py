import random

total = 1000000
ev = 0

for number in range(total):
    if random.randint(1, 6) == 2:
        ev += 1

print(ev / total)
