import turtle

from turtle import Turtle, Screen
from defer import return_value

j=0
k=0

# setting up the screen
wn=turtle.Screen()
wn.title("way_of_life")
wn.bgcolor("black")
wn.setup(width= 800, height= 800)
wn.tracer(0)

#creating a pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.hideturtle()
pen.penup()
pen.color("Green")
pen.goto(-300, 150)
# giving the instructions
text=list("Instructions:\n1.Enter the number of cells you want\nto be alive at start, max 8\n2.Select the boxes and the game will \nstart once you have finished your selection.")

for i in text:
    pen.write("")

# pen.write("Instructions:\n1.Enter the number of cells you want\nto be alive at start, max 8\n2.Select the boxes and the game will \nstart once you have finished your selection.", align="left", font=("Courier", 18, "normal"))
wn.update()
# pen.clear()



# # creating a cell
# def create():
#     cell=turtle.Turtle()

#     cell.resizemode("user")
#     cell.turtlesize(0.5, 0.5)
    
#     cell.speed(0)
#     cell.color("white")
#     cell.shape("square")
#     cell.hideturtle()
#     cell.penup()

#     return cell

#updating the screen
def updates(x, y):
    global pen
    pen.clear()
    wn.tracer(1)

# getting the coordinates
def get_coor(x,y):
    global k
    k= int((x+380)/40)
    global j 
    j= int((380-y)/40)
    return x, y




class cells(Turtle):

    def __init__(self):
        super().__init__(shape="square", visible=True)
        # self.turtle=turtle.Turtle()
        self.speed(0)

        # self.shapesize(0.5)

        self.color("white")
        # self.hideturtle()
        # self.shape("square")
        self.penup()


# creating the lists
# list of lists
out=[]
bi= []

# lists for turtles
for i in range (0, 20, 1):
    list=[]
    out.append(list)
    arr=[0 for i in range(20)]
    bi.append(arr)

# cell= cells()

# creating the turtles
for list in out:
    for i in range (0, 20, 1):
        # cell= create()
        cell= cells()
        cell.goto(-380+k*40, 380-(i*40))
        list.append(cell)
        # list[i][k].goto((-390+k*20, 390-(i*20)))

    k+=1

turtle.onscreenclick(updates)

# turtle.mainloop()

# # GAME
# n= int(turtle.numinput("Enter the number of cells", ""))
# # wn.update()

# def break_sel()

# selecting turtles
def tur_sel():
    y=True
    while True:
        turtle.onscreenclick(get_coor)
        bi[k][j]=1
        out[k][j].color("red")
        wn.listen()
        wn.onkeypress('Return', y= False)
        wn.update()
        wn.mainloop()

# for i in range(n):



turtle.done()