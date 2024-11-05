import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.title("__Snake Game__")
screen.setup(width=600,height=600)
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
game_is_on=1

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.update_core()
        snake.extend()

    if snake.head.xcor() >280 or snake.head.xcor()<-280 or snake.head.ycor()>250 or snake.head.ycor()<-280:
        game_is_on=0
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            game_is_on=False
            scoreboard.game_over()
screen.exitonclick()
