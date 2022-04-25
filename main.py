from turtle import *

from draw import *

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("DRAWING GAME")

should_continue = True



'''OOP CODES GOES HERE'''
tim = Tim(screen)
tim.check()




screen.exitonclick()