import turtle
import time


def draw_traffic_light():

    turtle.penup()
    turtle.goto(-140, 220)
    turtle.pendown()
    turtle.color("dim gray")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(450)
        turtle.right(90)
    turtle.end_fill()

    # Draw the traffic lights
    draw_colored_circle("DarkRed", 50, -50, 150)
    draw_colored_circle("yellow3", 50, -50, 0)
    draw_colored_circle("green4", 50, -50, -150)


def draw_colored_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()

    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(radius + 1)
    turtle.end_fill()

    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x, y - (radius + 5)) 
    turtle.pendown()
    turtle.color("black")
    turtle.circle(radius + 7)  

def control_traffic_lights():
    while True:

        draw_colored_circle("red", 50, -50, 150)
        time.sleep(10)


        draw_colored_circle("DarkRed", 50, -50, 150)

        draw_colored_circle("yellow", 50, -50, 0)
        time.sleep(3)


        draw_colored_circle("yellow3", 50, -50, 0)


        draw_colored_circle("green", 50, -50, -150)
        time.sleep(10)


        draw_colored_circle("green4", 50, -50, -150)


        draw_colored_circle("yellow", 50, -50, 0)
        time.sleep(5)


        draw_colored_circle("yellow3", 50, -50, 0)


turtle.speed(0)
turtle.hideturtle()
turtle.title("Traffic Light Simulation")
turtle.bgcolor("black")


while True:

    draw_traffic_light()


    control_traffic_lights()


    turtle.clear()
