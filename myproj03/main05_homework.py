"""
1 이상 100미만 범위에서 3과 5의 공배수를 모두 출력하기
"""

# 1
for i in range(1, 100):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i)


# 2
for i in range(1, 100):
    if i % 15 == 0:
        print(i)


# 3
for i in range(15, 100, 15):
    print(i)
