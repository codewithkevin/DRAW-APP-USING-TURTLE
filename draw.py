from turtle import Turtle

SQUARE = 4
TRIANGLE = 3
CIRCLE = 2

DRAW_LIST = ['triangle', 'square', 'circle']
EXIST_LIST = ['stop', 'n', 'nope', 'exist']


class Tim(Turtle):

    def __init__(self, display):
        super().__init__()
        self.display = display
        self.should_continue = True
        self.shape("turtle")
        self.color("white")
        self.goto(-40, 0)
        self.choice = self.display.textinput(title="WHAT DOYOU WANT TO DRAW", prompt='Enter your response;\n')

    def  check(self):
        while self.should_continue:
            def game(number_of_side):
                angle = 360 / number_of_side
                for _ in range(number_of_side):
                    self.forward(100)
                    self.left(angle)

            for shape in DRAW_LIST:
                if self.choice == shape:
                    if shape == 'triangle':
                        game(TRIANGLE)
                    elif shape == 'square':
                        game(SQUARE)
                    elif shape == 'circle':
                        game(CIRCLE)
                    else:
                        self.display.textinput(title="WHAT DOYOU WANT TO DRAW", prompt='Enter your response;\n')

            
            
            
