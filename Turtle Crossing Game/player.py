from turtle import Turtle

STARTING_POSITION = (0, -280)


class Player(Turtle):
    """Player turtle."""
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self):
        self.forward(20)

    def reset_position(self):
        self.goto(STARTING_POSITION)
