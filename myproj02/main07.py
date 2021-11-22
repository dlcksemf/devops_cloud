def calculate_sum(max_number):
    accmulator = 0
    for i in range(1, max_number):
        accmulator += i
    return accmulator


print(calculate_sum(100))
