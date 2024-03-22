import turtle
import colorsys
import random

t = turtle.Turtle()
t.hideturtle()  
t.screen.bgcolor("black")
t.speed(0)
t.width(2)

def draw_star(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def random_color():
    h = random.random()
    s = 0.8
    v = 0.8
    return colorsys.hsv_to_rgb(h, s, v)

def draw_pattern(num_stars, max_size, color_increment):
    for _ in range(num_stars):
        c = random_color()
        size = random.randint(50, max_size)
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        draw_star(x, y, size, c)

draw_pattern(50, 100, 0.05)

turtle.done()
