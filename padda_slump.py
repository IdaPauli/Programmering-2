import turtle
import random 

p = turtle.Turtle()

for i in range(20):
    steg = random.randint(1,100)
    vinkel = random.randint(1,360)
    p.fd(steg)
    p.left(vinkel)

p.screen.mainloop()