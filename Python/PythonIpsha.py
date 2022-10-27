from turtle import Turtle, Screen
screen = Screen()
t = Turtle()
t.penup()
t.hideturtle()
s = str(screen.textinput(title="Enter", prompt="What do you want to drink?"))
if s == 'coffee':
    s = 'code'
t.write(s, True, align="center", font=("Times New Roman", 20, 'normal'))
screen.exitonclick()
