import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비되셨으면, 엔터키를 입력해주세요.")

# random.shuffle(animal_names)

begin_time = time.time()

ok_counter = 0
word_counter = 0

random_name = random.sample(animal_names, k=5)

# for random_name in animal_names[0:5]:
for count in range(5):
    print(random_name[count])
    line = input(">>> ")
    if random_name[count] == line:
        ok_counter += 1
        print("정확합니다.")
        word_counter += len(random_name[count])
    else:
        print("오타가 있어요.")

end_time = time.time()

type_speed = 60 // (end_time - begin_time) * word_counter

print(f"{ok_counter}번 성공하셨습니다!")
print(f"총 {end_time - begin_time}초가 결리셨어요.")
print(f"분당 타자수는 {type_speed}입니다!")
