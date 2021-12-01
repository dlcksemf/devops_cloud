import random
import time

choices = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
numbers = random.sample(range(0, 8), 5)
question = [choices[number] for number in numbers]

question_number = 1
print("[타자게임] 준비되면 엔터!")
input()
start = time.time()

while question_number <= 5:
    print("*문제", question_number)
    print(question[question_number - 1])
    answer = input()

    if question[question_number - 1] == answer:
        print("정답!")
        question_number += 1
    else:
        print("오타! 다시 도전")

end = time.time()
time = format(end - start, ".2f")
print(f"타자시간: {time}초")
