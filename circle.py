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
