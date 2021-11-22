import turtle as t


# def polygon(n):
#     for x in range(n):
#         t.forward(50)
#         t.left(360 / n)


# def polygon2(n, a):
#     for x in range(n):
#         t.forward(a)
#         t.left(360 / n)


# polygon(3)
# polygon(5)

# t.up()
# t.forward(100)
# t.down()

# polygon2(3, 75)
# polygon2(5, 100)

t.bgcolor("black")
t.speed(0)

for x in range(200):
    if x % 3 == 0:
        t.color("red")
    elif x % 3 == 1:
        t.color("yellow")
    else:
        t.color("blue")
    t.forward(x * 2)
    t.left(119)
