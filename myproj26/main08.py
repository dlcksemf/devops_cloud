
# name, *rest = ["Tom", 10, "Seoul"]

# print(name)
# print(rest)


numbers = [1, 2, 3]

new_numbers = [
    10, 20, 30,
    *numbers,
    40, 50, 60,
    *numbers,
    70, 80, 90,
    *numbers,
]

print(new_numbers)


tom = {
    "name": "Tom",
    "age": 10,
    "region": "Seoul"
}


# steve는 tom과 age/region이 같아요.
# tom을 참조하여 name만 변경해서
# 새로운 steve를 만들고자 합니다.
steve = dict(tom, name="Steve")

print(steve)