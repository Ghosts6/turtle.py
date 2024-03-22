import turtle
import colorsys


t = turtle.Turtle()
t.hideturtle()  
t.screen.bgcolor("black")
t.speed(0)
t.width(2)


def draw_spiral(num_turns, start_size, angle_increment, color_increment):
    t.penup()
    t.goto(0, 0)  
    t.pendown()
    
    h = 0  
    for _ in range(num_turns):
        c = colorsys.hsv_to_rgb(h, 1, 1)  
        t.color(c)
        t.begin_fill()  
        for _ in range(4):  
            t.forward(start_size)
            t.right(90)
        t.end_fill() 
        t.right(angle_increment)  
        start_size += angle_increment  
        h += color_increment  


draw_spiral(100, 10, 5, 0.01)

turtle.done()
