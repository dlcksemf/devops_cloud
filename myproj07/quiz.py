"""
Quiz: 지전 조건의 인자만 처리하기
    filter_fn을 통과하지 못하는 인자는 alter_value 값으로 대체해봅시다.
"""


def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            new_args = list()
            for number in args:
                if filter_fn(number):
                    number = alter_value
                new_args.append(number)
            return fn(*new_args)

        return inner

    return wrap


@myfilter(lambda i: i % 2 == 0, 0)
def mysum(a, b, c, d, e):
    return a + b + c + d + e


@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e


print(mysum(1, 2, 3, 4, 5))

print(mymultiply(1, 2, 3, 4, 5))
