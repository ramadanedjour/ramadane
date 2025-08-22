from turtle import *
import colorsys as cs
tracer(20)
bgcolor(blue)
h=0.2
pensize=(1)
for i in range (1,100):
    c=cs.hsv_to_rgb(hi,100,0.6)
    h+=0.002
    color(c)
    circle(100,-i,70)
    left(18)
    done()
