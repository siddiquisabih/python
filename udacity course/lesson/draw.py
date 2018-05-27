import turtle


def drawSquare(tur):
    for a in range(1 , 5):
        tur.forward(100)
        tur.right(90)



def draw():
 window = turtle.Screen()
 window.bgcolor('red')
 bob = turtle.Turtle()
 bob.shape('turtle')
 bob.color('yellow')
 bob.speed(40)

 for abc in range(1,37):
    drawSquare(bob)
    bob.right(10)



 window.exitonclick()


draw()