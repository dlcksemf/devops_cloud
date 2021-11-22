# break 사용
for number in range(2, 10):
    print(f"### {number}단 ###")
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")
        if i == number:
            break
    print("")


# break 사용 안함
# for number in range(2, 10):
#     print(f"### {number}단 ###")
#     for i in range(1, number + 1):
#         print(f"{number} * {i} = {number * i}")
#     print("")
