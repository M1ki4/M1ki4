from turtle import *

w = Screen()

w.setup(1000,750)

w.bgcolor('black')

T = Turtle()

T.color('red')

T.speed(0)

T.hideturtle()

def square(L):
    if L < 0:
        return
    for i in range(4):
        T.forward(L)
        T.left(90)
        
    T.left(18)
    return square(L-1)

square(200)


mainloop()