life = {
    "animals": {"cats": ["Henri", "Grumpy", "Lucy"], "octopi": {}, "emus": {}},
    "plants": {},
    "other": {},
}

print(life.keys())
print(life["animals"].keys())
print(life["animals"]["cats"])

squares = {number: number ** 2 for number in range(10)}

odd_set = {number for number in range(10) if number % 2 == 1}

for thing in ("Got %s" % number for number in range(10)):
    print(thing)
keys = ("optimist", "pessimist", "troll")
values = (
    "The glass is half full",
    "The glass is half empty",
    "How did you get a glass?",
)

dict(zip(keys, values))
