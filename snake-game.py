import turtle
import time 

delay = 0.1

#Screen size 
wn = turtle.Screen()
wn.title("Snake Game By Justin")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)


# Making the snakehead
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "down"


#Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


#Main game loop
while True:
    wn.update()
    
    move()

    time.sleep(delay)

wn.mainloop()