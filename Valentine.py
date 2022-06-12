import turtle

td = turtle.turtles()
turtle.pencolor("red")

def curva():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


def core():
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(113)
    curva()
    turtle.left(120)
    curva()
    turtle.forward(112)
    turtle.end_fill()


def txt():
    turtle.up()
    turtle.setpos(-68, 95)
    turtle.down()
    turtle.color('black')
    turtle.write('FELIZ DIA DOS NAMORADOS')

core()
txt()

turtle.ht()
turtle.getscreen().mainloop()