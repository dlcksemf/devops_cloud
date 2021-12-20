
# 변수
name = "이찬들" # 선언
name = "Steve" # 변경



# 제어구조
number = 10

if number % 2 == 0:
    print("짝수")
else:
    print("홀수")


# 반복문
for i in range(1,11):
    print(i)

for i in range(1, 11, 2):
    print(i)


# 함수
def mysum(x, y):
    return x + y

print(mysum(1, 2))

mysum2 = lambda x, y: x + y
print(mysum2(1, 2))


def mysum5(x, y, *args):
    return x + y + sum(args)

print(mysum5(1, 2, 3, 4, 5))