from turtle import *
t= Turtle()

def retangulo(x, y, largura, altura, cor):
    t.color(cor)
    t.penup()
    t.goto(x, y)
    t.setheading(90)  # garante que começa reto
    t.pendown()
    for _ in range(2):
        t.forward(altura)
        t.left(90)
        t.forward(largura)
        t.left(90)
retangulo(0, 150, 440, 150, 'black')
t.begin_fill()
t.fillcolor('red')
retangulo(0, 0,440,150, 'red')
t.end_fill()

mainloop()
