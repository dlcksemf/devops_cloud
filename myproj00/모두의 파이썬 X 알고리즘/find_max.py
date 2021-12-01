def find_max(a):
    n = len(a)
    max_v = a[0]
    index = 0
    for number in range(1, n):
        if a[number] > max_v:
            max_v = a[number]
            index = number
    return max_v, index


def find_max2(numbers, length):
    if length == 1:
        return numbers[0]
    max_number = find_max2(numbers, length - 1)
    if max_number > numbers[length - 1]:
        return max_number
    else:
        return numbers[length - 1]


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))
print(find_max2(v, len(v)))
