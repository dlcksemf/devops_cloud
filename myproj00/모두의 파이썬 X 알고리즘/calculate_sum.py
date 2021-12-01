def calculate_sum(max_number: int):
    acc = 0
    for number in range(max_number + 1):
        acc += number
    return acc


def calculate_sum_simple(max_number: int):
    return max_number * (max_number + 1) // 2


def calculate_sum3(max_number):
    if max_number == 1:
        return 1
    return max_number + calculate_sum3(max_number - 1)


number = int(input("=>  "))
print(f"{number}까지 총 합은 {calculate_sum(number)}입니다.")
print(f"{number}까지 총 합은 {calculate_sum_simple(number)}입니다.")
print(f"{number}까지 총 합은 {calculate_sum3(number)}입니다.")
