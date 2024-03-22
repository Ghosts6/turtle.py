![baner](https://github.com/Ghosts6/Local-website/blob/main/img/Baner.png)

# 🖱️Turtle exercise:

some simple code that i write to learn about turtle library and differend method and usage of it

# code sample:

```python
from turtle import*
import colorsys
bgcolor('black')
tracer(200)
def draw():
    h=0
    n=200
    for i in range (2,2900):
     c = colorsys.hsv_to_rgb(h,1,1)
     h += 1/n
     goto(0,0)
     down()
     color(c)
     pensize(8)
     circle(i,100)
draw()
done()
```

```python
import turtle
import colorsys
t = turtle.Turtle()
t.screen.bgcolor("black")

t.penup()
t.goto(-200,-100)
t.pendown()
t.speed(10)
print("enter number of triangles:",'\n')
a=400 ; h=0; n=100
def triangle():
    global a,n,h
    for i in range(40):
        c = colorsys.hsv_to_rgb(h,1,0.6)
        h = h+(1/n)
        t.color(c)
        t.forward(a)
        t.left(120)
        a = a-10
    
triangle()
triangle()
triangle()
triangle()
```

# 📹video:
