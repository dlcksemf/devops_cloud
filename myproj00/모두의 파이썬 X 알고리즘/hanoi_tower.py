def hanoi_tower(number):
    if number == 1:
        return 1
    elif number == 2:
        return 3
    return (hanoi_tower(number - 1) * 2) + 1


print(hanoi_tower(4))
print(hanoi_tower(5))
