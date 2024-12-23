import turtle

turtle.Screen().bgcolor("blue")
board = turtle.Turtle()
 
# first triangle for star
board.fillcolor("red")
board.begin_fill()
board.forward(100) # draw base
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)
board.end_fill()

board.penup()
board.right(150)
board.forward(50)
 
# second triangle for star
board.fillcolor("red")
board.pendown()
board.right(90)
board.forward(100)
 
board.right(120)
board.forward(100)
 
board.right(120)
board.forward(100)
board.end_fill
 
turtle.done()
