import turtle
import random 

pen = turtle.Turtle()
turtle.Screen().colormode(255)
turtle.Screen().tracer(1,1)
turtle.screensize(canvwidth=800, canvheight=800)
turtle.ht()

ncirc = 5
ref = 5

pos_list = []
col_list = []

def rand_col():
    for i in range(ncirc):
        pencolr = random.randint(0, 255)
        pencolg = random.randint(0, 255)
        pencolb = random.randint(0, 255)
        col = list((pencolr, pencolg, pencolb))
        col_list.append(col)
    return col_list
col_list = rand_col()

def rand_pos():
    for i in range(ncirc):
        penposx = random.randint(-300, 300)
        penposy = random.randint(-300, 300)
        pos = list((penposx, penposy))
        pos_list.append(pos)
    return pos_list
pos_list = rand_pos()

class draw_circ:
    def __init__(self, pos, fillcol, collist):
        self.rad = 40
        self.circpos = pos
        self.fillcol = fillcol
        self.pencol = 'black'
        self.collist = collist
    
    def change_col(self):
        a = 0
        r = random.randint(0,ncirc-1)
        print(r)
        for a in range(ncirc):
            print(self.collist)
            print(r)
            print(a)
            #print(self.collist[a][0] + self.collist[r][0])
            self.collist[a][0] = self.collist[a][0] + self.collist[r][0]
            self.collist[a][1] = self.collist[a][1] + self.collist[r][1]
            self.collist[a][2] = self.collist[a][2] + self.collist[r][2]
            if self.collist[a][0] > 255:
                self.collist[a][0] -= 255
            if self.collist[a][1] > 255:
                self.collist[a][1] -= 255
            if self.collist[a][2] > 255:
                self.collist[a][2] -= 255
    
    def circ(self):
        turtle.color(self.pencol, self.fillcol)
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(self.circpos)
        turtle.pendown()
        turtle.circle(self.rad)
        turtle.end_fill()
print(col_list)
for i in range(ncirc):
    cir = draw_circ(pos_list[i], col_list[i], col_list)
    cir.circ()
    turtle.Screen().update()

for j in range(ref):
    cir.change_col()
    for i in range(ncirc):
        cir = draw_circ(pos_list[i], col_list[i], col_list)
        cir.circ()
        turtle.Screen().update()

turtle.done()