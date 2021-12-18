from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(car.car_speed)
    car.move()
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_level()
        car.increase_speed()
    for each_car in car.cars:
        if each_car.xcor() < -320:
            each_car.goto(x=320, y=random.randint(-200, 200))
        if each_car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
