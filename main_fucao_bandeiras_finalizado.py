import math
from turtle import *
from time import sleep 
t= Turtle()
t.speed(15)
t.hideturtle()

def triangulo(x, y, cateto, base, color):
    t.color('black')
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.rt(135)
    t.fd(cateto)
    t.rt(90)
    t.fd(cateto)
    t.rt(135)
    t.fd(base)
    t.end_fill()

def retangulo_vertical(x, y, larg, alt, color):
    t.pu()
    t.goto(x,y)
    t.setheading(90)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()

def estrela(x,y, ang, lado_estrela, lado1, lado2,lado3,lado4, color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(5):
        t.fd(lado_estrela) 
        t.rt(ang) 
    t.end_fill()
    t.begin_fill()
    t.fillcolor('black')
    t.fd(lado1)
    t.rt(90)
    t.fd(lado2)
    t.rt(90)
    t.fd(lado3)
    t.rt(90)
    t.fd(lado4)
    t.end_fill()

def retangulo_horizontal(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.setheading(90)  
    t.pd()
    t.color('black')
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(alt)
        t.lt(90)
        t.fd(larg)
        t.lt(90)
    t.end_fill()

def circulo(x, y, ang, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(ang)
    t.end_fill()

def folha_canada(x,y, color):
    t.color(color)  
    escala = 0.5
    pontos = [
        (0*escala, 150*escala), (20*escala, 80*escala), (60*escala, 100*escala),
        (40*escala, 40*escala), (100*escala, 30*escala), (30*escala, -10*escala),
        (50*escala, -80*escala), (0*escala, -40*escala), (-50*escala, -80*escala),
        (-30*escala, -10*escala), (-100*escala, 30*escala), (-40*escala, 40*escala),
        (-60*escala, 100*escala), (-20*escala, 80*escala)
    ]
    t.penup()
    t.goto(pontos[0])
    t.pendown()
    t.begin_fill()
    for p in pontos:
        t.goto(p)
    t.goto(pontos[0])
    t.end_fill()
    t.penup()
    t.goto(x, y * escala)
    t.setheading(-90)
    t.pendown()
    t.width(6 * escala)
    t.color(color)  
    t.forward(60 * escala)

def japao():
    retangulo_horizontal(0, 0, 400, 250,'white')
    circulo(-132,125, 65, 'red')

def polonia():
    retangulo_horizontal(100, 150, 480, 150, 'white')
    retangulo_horizontal(100, 0, 480, 150, 'red')

def arabes_unidos():
    retangulo_vertical(-200,0, 240, 100, 'red')
    retangulo_horizontal(180,0,280, 80, 'black')
    retangulo_horizontal(180,80,280, 80, 'white')
    retangulo_horizontal(180,160,280, 80, 'dark green')

def indonesia():
    retangulo_horizontal(100, 150, 480, 150, 'red')
    retangulo_horizontal(100, 0, 480, 150, 'white')

def holanda():
    retangulo_horizontal(180,0,340, 80, 'blue')
    retangulo_horizontal(180,80,340, 80, 'white')
    retangulo_horizontal(180,160,340, 80, 'red')

def iemen():
    retangulo_horizontal(180,0,340, 80, 'black')
    retangulo_horizontal(180,80,340, 80, 'white')
    retangulo_horizontal(180,160,340, 80, 'red')

def austria():
    retangulo_horizontal(180,0,340, 80, 'red')
    retangulo_horizontal(180,80,340, 80, 'white')
    retangulo_horizontal(180,160,340, 80, 'red') 

def bahamas():
    retangulo_horizontal(180,0,340, 80, '#00a8ff')
    retangulo_horizontal(180,80,340, 80, 'yellow')
    retangulo_horizontal(180,160,340, 80, '#00a8ff')
    triangulo(-160,240, 170, 240, 'black')

def palestina():
    retangulo_horizontal(180,0,340, 80, 'dark green')
    retangulo_horizontal(180,80,340, 80, 'white')
    retangulo_horizontal(180,160,340, 80, 'black')
    triangulo(-160,240, 170, 240, 'red')

def sudao():
    retangulo_horizontal(180,0,340, 80, 'black')
    retangulo_horizontal(180,80,340, 80, 'white')
    retangulo_horizontal(180,160,340, 80, 'red')
    triangulo(-160,240, 170, 240, 'dark green')

def grecia():
    retangulo_horizontal(100, 0, 300, 17,'#4176e1')
    retangulo_horizontal(100, 17, 300, 17,'white')
    retangulo_horizontal(100, 34, 300, 17,'#4176e1')
    retangulo_horizontal(100, 51, 300, 17,'white')
    retangulo_horizontal(100, 68, 300, 17,'#4176e1')
    retangulo_horizontal(100, 85, 300, 17,'white')
    retangulo_horizontal(100, 102, 300, 17,'#4176e1')
    retangulo_horizontal(100, 119, 300, 17,'white')
    retangulo_horizontal(100, 136, 300, 17,'#4176e1')
    retangulo_horizontal(-125, 85, 75, 68,'#4176e1')
    retangulo_horizontal(-157, 85, 10, 68,'white')
    retangulo_horizontal(-125, 115, 75, 10,'white')

def saotome_principe():
    retangulo_horizontal(180,0,340, 80, 'green')
    retangulo_horizontal(180,80,340, 80, 'yellow')
    retangulo_horizontal(180,160,340, 80, 'green')
    triangulo(-160,240, 170, 240, 'red')
    estrela(20, 90, 144, 55, 38,20,22,20, 'black')
    estrela(140, 110, 144, 55, 38,20,22,20, 'black')

def folha_canada(x,y, color):
    t.color(color)  
    escala = 0.5
    pontos = [
        (0*escala, 150*escala), (20*escala, 80*escala), (60*escala, 100*escala),
        (40*escala, 40*escala), (100*escala, 30*escala), (30*escala, -10*escala),
        (50*escala, -80*escala), (0*escala, -40*escala), (-50*escala, -80*escala),
        (-30*escala, -10*escala), (-100*escala, 30*escala), (-40*escala, 40*escala),
        (-60*escala, 100*escala), (-20*escala, 80*escala)
    ]
    t.penup()
    t.goto(pontos[0])
    t.pendown()
    t.begin_fill()
    for p in pontos:
        t.goto(p)
    t.goto(pontos[0])
    t.end_fill()
    t.penup()
    t.goto(x, y * escala)
    t.setheading(-90)
    t.pendown()
    t.width(6 * escala)
    t.color(color)  
    t.forward(60 * escala)

def canada():
    folha_canada(0, -40, 'red')
    retangulo_vertical(-195, -92, 220, 70, 'red')
    retangulo_vertical(130, -92, 220, 70, 'red')

#japao
japao()
sleep(3)
t.clear()

#polonia
polonia()
sleep(3)
t.clear()

#arabes unidos
arabes_unidos()
sleep(3)
t.clear()

indonesia()
sleep(3)
t.clear()

#holanda
holanda()
sleep(3)
t.clear()

#iemen
iemen()
sleep(3)
t.clear()

#austria
austria()
sleep(3)
t.clear()

#bahamas
bahamas()
sleep(3)
t.clear()

#palestina
palestina()
sleep(3)
t.clear()

#sudao
sudao()
sleep(3)
t.clear()

#grecia
grecia()
sleep(3)
t.clear()

#sao tome e principe
saotome_principe()
sleep(3)
t.clear()

#canada
canada()
sleep(3)
t.clear()

mainloop()
