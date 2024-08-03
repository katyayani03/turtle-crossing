import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    # detect when player reached the other side
    if player.at_finish_line(): #if level completed
        player.go_to_start() #start another level
        car_manager.increase_speed() #increase car speed
        scoreboard.increase_level()

screen.exitonclick()
