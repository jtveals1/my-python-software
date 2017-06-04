#Jason Veals
#6-25-2016
#Snowman - Fun with Graphics
#This program uses Python graphics to draw a snowman

from turtle import *

def main():
    reset()
    drawFace()
    drawBody()
    drawArms()
    drawHat()
    ht()               # turn off the turtle
    return "Done!"

def draw_circle(x, y, radius, color1):
    setpos(x,y-radius)  #draws from bottom up, so shift down to center at x,y
    setheading(0)       #east
    down()              # Pen down, start drawing
    begin_fill()        #   fill the shape that starts here
    color (color1, color1)
    circle (radius, 360)
    end_fill()          #   fill the shape that ended here
    up()                # Pen up, stop drawing


    #draws face
def drawFace():   
    draw_circle (0, 90, 60, "yellow")
    draw_circle (-20, +110, 5, "white")
    draw_circle (+20, +110, 5, "white")
    
    # Draw the mouth
    setpos (-30, 70)
    setheading(315)       # Southeast
    down()
    color ("black","black")
    circle (40, 90)         # Draw 1/4 of a circle (90 degrees only)
    up()
    drawNose()
        


    #draws the body
def drawBody():
    draw_circle (0, -30, 60, "blue")
    draw_circle (0, -150, 60, "black")

    #draws the buttons
    draw_circle( 0, 0, 5, "red")
    draw_circle( 0, -30, 5, "red")
    draw_circle( 0, -60, 5, "red")

    #draws arms
def drawArms():
    setpos(50,5)
    setheading(315)
    down()
    color("black")
    width(5)
    forward(100)
    up()
    
    setpos(-50,5)
    down()
    backward(100)
    width(0)
    up()

    #draws hat
def drawHat():
    setpos(-95,150)
    setheading(0)
    down()
    begin_fill()
    forward(200)
    left(90)
    forward(5)
    left(90)
    forward(200)
    left(90)
    forward(5)
    end_fill()
    up()

    setpos(-40,155)
    setheading(90)
    down()
    begin_fill()
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    end_fill()
    up()

#draws nose
def drawNose():
    setheading(0)
    setpos(-7,80)
    down()
    width(3)
    forward(14)
    width(0)
    up()
    
if __name__ == '__main__':
    main()
    mainloop()

