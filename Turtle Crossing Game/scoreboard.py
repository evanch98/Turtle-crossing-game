from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """Scoreboard to display level and game over."""
    def __init__(self):
        super().__init__()
        # Starting Level
        self.level = 1
        # To display level
        self.penup()
        self.hideturtle()
        self.goto(x=-250, y=270)
        self.update_scoreboard()

    def increase_level(self):
        """Increase level by adding 1 to self.level everytime this method is called."""
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the previous level text and update the current level text."""
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        """Display 'Game Over.' when this method is called."""
        self.goto(-80, 0)
        self.write(arg=f"Game Over.", font=FONT)
