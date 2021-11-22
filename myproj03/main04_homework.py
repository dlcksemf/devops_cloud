"""
반복문을 활용하여, 효과적으로 3단/6단/9단 구구단 출력하기
"""

for number in range(3, 10, 3):
    print(f"###   {number}단   ")
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")
    print("")
