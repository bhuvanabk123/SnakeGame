
import time
from snake import *
from food import *
from turtle import Screen
from scoreboard import  *

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True



while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        snake.extend()
        scoreboard.increase_score()


    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()