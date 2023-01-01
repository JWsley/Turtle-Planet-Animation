import turtle


turtle.title("Planet animation")

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.pencolor('red')                                

x = 0
y = 0
t.speed(0)
t.penup()
t.goto(0,200)                                                              
t.pendown()
while True:

    t.forward(x)
    t.right(y)
    x+=3
    y+=1

    if y == 210:
        break
    t.hideturtle()


turtle.done()
