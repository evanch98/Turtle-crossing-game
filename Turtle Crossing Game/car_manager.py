from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


def random_color():
    """Returns random rgb value."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_position():
    """Returns random (x,y) coordinate."""
    x = random.randint(-280, 320)
    y = random.randint(-200, 200)
    return x, y


class Car:
    def __init__(self):
        """Create 40 turtles at different positions each moving towards the left by 2px."""
        self.cars = []
        self.create_car()
        self.car_speed = 0.1

    def create_car(self):
        """Append new turtles to self.cars."""
        for _ in range(40):
            self.add_car(random_position())

    def add_car(self, position):
        """Create new turtle with different colors."""
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=1.5)
        new_car.color(random_color())
        new_car.penup()
        new_car.goto(position)
        self.cars.append(new_car)

    def move(self):
        """Moving towards the left by 2px."""
        for car in self.cars:
            new_x = car.xcor() - 2
            car.goto(x=new_x, y=car.ycor())

    def increase_speed(self):
        """To increase the speed."""
        self.car_speed *= 0.9
