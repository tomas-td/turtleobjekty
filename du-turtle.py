import turtle
from random import randrange

t = turtle.Turtle()


def hexagon():
    dlzka = randrange(10, 150)
    t.pencolor("red")
    t.pensize(7)


    for i in range(6):
        t.fd(dlzka)
        t.rt(60)

def trojuholnik():
    dlzka = randrange(10, 150)
    t.pencolor("blue")
    t.pensize(5)

    for i in range(3):
        t.fd(dlzka)
        t.rt(120)


def hviezda():
    dlzka = randrange(10,150)
    t.pencolor("orange")
    t.pensize(5)

    for i in range(5):
        t.fd(dlzka)
        t.rt(144)

def pozicia():
    x = randrange(-250, 250)
    y = randrange(-250, 250)
    uhol = randrange(360)
    t.setpos(x, y)
    t.rt(uhol)

for i in range(randrange(2,30)):
    t.penup()
    pozicia()
    t.pendown()
    objekt = randrange(0, 3)
    if (objekt == 1):
        hexagon()

    elif (objekt == 2):
        trojuholnik()

    else :
        hviezda()


turtle.exitonclick()