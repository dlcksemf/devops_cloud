number = int(input("?"))
prime = 2

while prime <= number:
    if number % prime == 0:
        print(prime)
        number /= prime
    else:
        prime += 1
