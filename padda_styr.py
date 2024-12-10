import turtle

screen = turtle.Screen()
screen.title("Styra padda")
screen.setup(width=600, height=600)

p = turtle.Turtle()

def upp():
    p.setheading(90)
    p.fd(20)

def höger():
    p.setheading(0)
    p.fd(20)

def vänster():
    p.setheading(180)
    p.fd(20)

def ner():
    p.setheading(270)
    p.fd(20)


screen.listen()
screen.onkeypress(upp, "Up")
screen.onkeypress(höger, "Right")
screen.onkeypress(vänster, "Left")
screen.onkeypress(ner, "Down")

p.screen.mainloop()
