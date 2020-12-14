from turtle import Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Fake Ass Snake Game")
# set screen tracer for drawing object
screen.tracer(0)
# listen to on key event
screen.listen()
# update frame
screen.update()


def choose_mode(user_mode):
    # return 0.1 when given string not in dict
    return{
        'hard': 0.05,
        'medium': 0.075,
        'easy': 0.1
    }.get(user_mode, 0.1)


def game_on():
    # create a snake
    snake = Snake()
    # set game mode
    mode = choose_mode(screen.textinput("Choose mode", prompt="Please enter mode['hard' 'medium' 'easy']: "))
    # create food
    food = Food()
    # create score board
    scoreboard = ScoreBoard()
    game_over = False
    while not game_over:
        # update the screen
        screen.update()

        # listen to event (button pressed)
        screen.listen()

        snake.move()
        # events
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")
        time.sleep(mode)

        # detect collision with food
        # diameter of a food is 10
        if food.distance(snake.head) < 15:
            snake.extend()
            food.refresh()
            scoreboard.increase_score()
        # detect collision with wall

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_over = True

        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) <= 5:
                game_over = True

    screen.update()
    scoreboard.print_final_score()
    screen.update()
    return scoreboard.score


# start game here
while True:
    game_on()
    cont = screen.textinput("GameOver", prompt="Continue?(yes or no):").lower()
    if cont == 'yes':
        screen.reset()
        continue
    else:
        break
screen.exitonclick()