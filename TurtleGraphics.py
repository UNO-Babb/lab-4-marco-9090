#TurtleGraphics.py
#Name: Marc Anthony Williasm
#Date: 9/22/204
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(sam, sides):
    for s in range(sides):
        sam.forward(80)
        sam.right(360/sides)
       
def fillCorner(gina, corner):  
    #draw big square
    drawSquare(gina, 200)
    
    if corner == 1:
        gina.begin_fill()
        drawSquare(gina, 100)
        gina.end_fill()      
    elif corner == 2:
        gina.forward(100)
        gina.begin_fill()
        drawSquare(gina, 100)
        gina.end_fill()
    elif corner == 3:
        gina.forward(100)
        gina.begin_fill()
        drawSquare(gina, 100)
        gina.end_fill()
        
def draw_square(a,x,y):
    penup()
    goto(x,y)
    setheading(90)
    backward(a//2)
    setheading(0)
    backward(a//2)
    pendown()
    for _ in range(4):
        forward(a)
        left(90)

draw_square(20,0,0)
draw_square(50,0,0)
draw_square(70,0,0)
draw_square(90,0,0)
draw_square(110,0,0)

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 200)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square with bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
