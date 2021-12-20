age = "..."

# 사전
tom = {
    "name": "Tom",
    "age": 10,
    # "ag" + "e": 10,
    age: 10,
}

name = "Tom"
age = 10

tom1 = {
    "name": name,
    "age": age,
}

# f-string => String Interpolation
print(f"""안녕 나는 {name}이야.
{age}살이지.""")