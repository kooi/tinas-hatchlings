import turtle
import random

step_size = 10
frame_time = 10000 // 60
screen_width = 500
screen_height = 500

food_lifetime = 100
food_timer = food_lifetime

screen = turtle.Screen()
screen.title("Tina's Hatchlings")
turtle.setup(width=screen_width, height=screen_height)
# screen.screensize(screen_width, screen_height)
tina = turtle.Turtle()
tina.shape("turtle")
tina.turtlesize(1.2)
tina.speed(0)

food = turtle.Turtle()
food.shape("square")
food.speed(0)
# food.hideturtle()
food.penup()


def make_food():
    global food_timer
    # if not food.isvisible() and food_timer == 0:
    if food_timer == 0 or not food.isvisible():
        food.showturtle()
        food_timer = food_lifetime
        x = step_size * random.randint(-screen_width / (2 * step_size),
                                       screen_width / (2 * step_size))
        y = step_size * random.randint(-screen_height / (2 * step_size),
                                       screen_height / (2 * step_size))
        food.setposition(x, y)
        # food.hideturtle()
    else:
        food_timer = food_timer - 1

def eat_food():
    t = tina.position()
    f = food.position()
    d = abs(t - f)
    # print("t:", t, "- f:", f, " - d:", d)
    if d < step_size:
        print("Nomnom")
        food.hideturtle()
        # add_score()
        # grow()


def do_step():
    # screen.update()
    tina.forward(step_size)
    eat_food()
    make_food()
    screen.ontimer(do_step, frame_time)


# screen.tracer(0)
screen.listen()
screen.onkey(lambda x=270: tina.setheading(x), "Down")
screen.onkey(lambda x=90: tina.setheading(x), "Up")
screen.onkey(lambda x=180: tina.setheading(x), "Left")
screen.onkey(lambda x=0: tina.setheading(x), "Right")
screen.ontimer(lambda: do_step(), frame_time)
screen.mainloop()
