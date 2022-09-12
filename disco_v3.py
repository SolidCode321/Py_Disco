import random as rand
import turtle
import time

pen = turtle.Turtle()
turtle.Screen().colormode(255)
turtle.Screen().tracer(1,1)
turtle.screensize(canvwidth=800, canvheight=800)
turtle.ht()

nocirc = 555
ref = 10
circ_array = []

def change_col(circ_array):
    a = 0
    r = rand.randint(0,nocirc-1)
    for a in range(nocirc):
        #print(circ_array[a].rgb_value[0] + circ_array[a].rgb_value[r][0])
        circ_array[a].rgb_value[0] = circ_array[a].rgb_value[0] + circ_array[r].rgb_value[0]
        circ_array[a].rgb_value[1] = circ_array[a].rgb_value[1] + circ_array[r].rgb_value[1]
        circ_array[a].rgb_value[2] = circ_array[a].rgb_value[2] + circ_array[r].rgb_value[2]
        if circ_array[a].rgb_value[0] > 255:
            circ_array[a].rgb_value[0] -= 255
        if circ_array[a].rgb_value[1] > 255:
            circ_array[a].rgb_value[1] -= 255
        if circ_array[a].rgb_value[2] > 255:
            circ_array[a].rgb_value[2] -= 255
    test()

class circl():
    def __init__(self):
        self.rad = 20
        self.pos = [rand.randint(-400,400), rand.randint(-400,400)]
        self.rgb_value = [rand.randint(0,255), rand.randint(0,255), rand.randint(0,255)]

for i in range(nocirc):
    circ_array.append(circl())

def circ():
    turtle.color("black", circ_array[i].rgb_value)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(circ_array[i].pos)
    turtle.pendown()
    turtle.circle(circ_array[i].rad)
    turtle.end_fill()

def test():
    for j in range(nocirc):
        print(circ_array[j].pos, end='')
        print(circ_array[j].rgb_value)
    print()

test()
for i in range(nocirc):
    turtle.Screen().tracer(False)
    circ()
    turtle.Screen().update()
#time.sleep(1)

for j in range(ref):
    for i in range(nocirc):
        turtle.Screen().tracer(False)
        change_col(circ_array)
        circ()
        turtle.Screen().update()
    time.sleep(1)
