import math
from turtle import *
def planeta(k):
    return 15*math.sin(k)**3
def planetb(k):
    return 12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3*k)-\
            math.cos(4*k)
speed(1000000000000000000000)
bgcolor("black")
for i in range(6000):
    goto(planeta(i)*20,planetb(i)*20)
    for j in range(5):
        color("#ff0000")
    goto(1,1)