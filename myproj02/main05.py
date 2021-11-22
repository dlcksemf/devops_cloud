def gugudan(number):
    print(f"### {number}단 ###")
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")


for i in range(2, 10):
    gugudan(i)
