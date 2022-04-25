from turtle import Turtle

SQUARE= 4
TRIANGLE = 3
CIRCLE = 2

DRAW_LIST = ['triangle', 'square', 'circle']
EXIST_LIST = ['stop', 'n', 'nope', 'exist']


class Tim(Turtle):

    def __init__(self, display):
        super().__init__()
        self.penup()
        self.display = display
        self.should_continue = True
        self.shape("circle")
        self.color("red")
        self.goto(-40, 0)
        self.choice = self.display.textinput(title="WHAT DOYOU WANT TO DRAW", prompt='Enter your response;\n')

    def  check(self):
        while self.should_continue:
            def game(number_of_side):
                angle = 360 / number_of_side
                for _ in range(number_of_side):
                    self.forward(100)
                    self.left(angle)

            if self.choice.lower() == "square":
                self.pendown()
                game(SQUARE)
                break
                

            elif self.choice.lower() == "triangle":
                self.pendown()
                game(TRIANGLE)
                break
                

            elif self.choice.lower() == "circle":
                self.pendown()
                game(CIRCLE)
                break

            elif 

            
            
