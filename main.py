from turtle import Turtle, Screen

tony = Turtle()
screen = Screen()

def move_forwards():
    tony.forward(10)

def move_backwards():
    tony.backward(10)

def turn_left():
    tony.left(15)

def turn_right():
    tony.right(15)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)

screen.exitonclick()