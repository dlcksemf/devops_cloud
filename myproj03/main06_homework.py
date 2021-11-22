"""
1 이상 100미만 범위에서 3과 5의 공배수의 합을 출력하기
"""

# 1
acc = 0

for i in range(1, 100):
    if (i % 3 == 0) and (i % 5 == 0):
        acc += i

print(acc)

# 2
number_list = []
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == o:
        number_list.append(i)
print(sum(number_list))
