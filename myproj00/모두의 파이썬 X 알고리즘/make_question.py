import random


def make_questions():
    # 문제 주기
    numbers = list(map(str, random.sample(range(1, 20), 2)))

    operation = random.randint(1, 3)
    if operation == 1:
        question = " + ".join(numbers)
    elif operation == 2:
        question = " - ".join(numbers)
    else:
        question = " * ".join(numbers)

    return question


right, wrong = 0, 0

for tries in range(5):
    question = make_questions()
    print(question)
    answer = int(input("=>  "))

    if eval(question) == answer:
        print("정답!")
        right += 1
    else:
        print("오답!")
        wrong += 1

print(f"정답: {right}, 오답: {wrong}")
if wrong == 0:
    print("당신은 천재입니다")
