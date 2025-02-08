import turtle
import time 
import random

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
head.direction = "stop"

# Making the snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []



#Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"



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



#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



#Main game loop
while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments: 
            segment.goto(1000, 1000)


            segments.clear()

    if head.distance(food) < 20: 
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #Add a segment for the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment)        


    for index in range(len(segments) -1, 0, -1):
            x = segments[index -1].xcor()
            y = segments[index -1].ycor()
            segments[index].goto(x,y)

    if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x,y)
    
    move()

    time.sleep(delay)

wn.mainloop()