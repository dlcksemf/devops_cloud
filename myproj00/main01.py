# 5.1
''' 
song = """When an eel grabs your arm,\nAnd it causes great harms,\nThar's - a moray!"""

song = song.replace(' m',' M')

print(song)
'''

# 5.2

'''questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]

answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

count = 0
while count < len(questions):
    print(count)
    print(questions[count])
    print('\n')
    print(answers[count])
    count += 1'''

# 5.3
'''
poem = "My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s And now thinks he's a %s.
"
args = ('roast beef', 'ham', 'head', 'clam')

print(poem % args)
'''

# 5.4
letter = '''
Dear {salutation} {name}
    Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially near any
{animals}.

    Send us your receipt and {amount} for shipping and handling. We will send you
another {product} that, in our tests, is {percent}% less likely to have {verbed}.

    Thank you for your support.
    Sincerely,
    {Spokeman}
    {job_title}
'''