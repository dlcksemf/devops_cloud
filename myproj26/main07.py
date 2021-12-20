

def mysum3(x, y, z):
    return x + y * 10 + z * 100

# 위치인자 
print(mysum3(1, 2, 3))

# 키워드 인자
print(mysum3(x=1, y=2, z=3))

kwargs = {"x": 1, "y": 2, "z": 3}
print(mysum3(**kwargs))

#...

people = [
  { "name": 'Tom', "age": 10, "region": 'Seoul' },
  { "name": 'Steve', "age": 12, "region": 'Pusan' }
]

for person in people:
    print(person["name"], person["age"])