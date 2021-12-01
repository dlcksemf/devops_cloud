# rows = range(1,4)
# cols = range(1,3)

# cells = [(row, col) for row in rows for col in cols]

# for cell in cells:
#     print(cell)

start1 = ["fee", "fie", "foe"]

rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]

start2 = "Someone better"

start1_caps = " ".join([word.capitalize() + "!" for word in start1])

for first, second in rhymes:
    print(f"{start1_caps} {first.capitalize()}!")
    print(f"{start2} {second}.")
