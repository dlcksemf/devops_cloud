def get_default_value():
    print("get-defautl-value()를 호출")
    return 10

# 함수 정의 시점에 호출이 된다.
# def hello(name, age=get_default_value()):
    # print(f"안녕 나는 {name}이야. {age}살이지.")


# 그러면, 파이썬에서 디폴트 값이 필요할 때 마다, 그 함수가 호출이되게 할려면???
def hello(name, age=None):
    if age is None:
        age = get_default_value()
    print(f"안녕 나는 {name}이야. {age}살이지.")

hello("Tom")
hello("Steve")
hello("John")