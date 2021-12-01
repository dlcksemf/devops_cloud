# # 1

# def good():
#     name_list = ["Harry", "Ron", "Hermione"]
#     return name_list


# print(good())

# # 2
# def get_odds(range):
#     first = 1
#     last = range[len(range) - 1]
#     while first <= last:
#         yield first
#         first += 2


# odds_list = get_odds(range(10))

# for x in odds_list:
#     print(x)

# # 3
# def test(func):
#     def wrapper(*args):
#         print(f"start {func.__name__}")
#         func(*args)
#         print(f"end {func.__name__}")

#     return wrapper


# @test
# def hello_func():
#     print("hello")


# hello_func()

# 4
class OopsException(Exception):
    pass


number = int(input("=>  "))

if number % 2 == 0:
    raise OopsException("panic")
else:
    print("No Error")
