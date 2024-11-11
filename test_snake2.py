import turtle
import time
import random
import winsound

delay = 0.1
score = 0
hs_file = open("highest_score_game.text", "r")
# high_score = int(hs_file.read())

# frame of screen
frm = turtle.Screen()
frm.title("Snake Game By Priyam")
frm.bgcolor("grey")
frm.setup(width=600, height=600)
frm.tracer(0)

#  snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

# food
food = turtle.Turtle()
# colors = random.choice(['red', 'green', 'black'])
food.shape("circle")
food.color(random.choice(['green', 'yellow', 'orange']))
food.penup()
food.goto(0, 100)

# # score board
# sb = turtle.Turtle()
# sb.color("black")
# sb.penup()
# sb.ht()
# sb.goto(-270, -270)
# sb.write("Score: 0 | highest Score : 0")

  
# food_eat_sound
def food_sound():
    winsound.PlaySound("boing_spring.wav", winsound.SND_ASYNC)
    
# game over sound 
def game_over():
    winsound.PlaySound("alarm_beep.wav", winsound.SND_ASYNC)
    

#not posible move
def moveup():
    if snake.direction != "down":
        snake.direction = "up"


def movedown():
    if snake.direction != "up":
        snake.direction = "down"


def moveleft():
    if snake.direction != "right":
        snake.direction = "left"


def moveright():
    if snake.direction != "left":
        snake.direction = "right"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


frm.listen()
frm.onkeypress(moveup,"Up")
frm.onkeypress(movedown, "Down")
frm.onkeypress(moveleft, "Left")
frm.onkeypress(moveright, "Right")

snake_body = []

while True:
    frm.update()
    if snake.xcor() > 290:
        snake.setx(-290)
    if snake.xcor() < -290:
        snake.setx(290)
    if snake.ycor() > 290:
        snake.sety(-290)
    if snake.ycor() < -290:
        snake.sety(290)

    if snake.distance(food) < 20:
        food_sound()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Adding new food in tail
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("red")  # tail colour
        new_tail.penup()
        snake_body.append(new_tail)

        # update score
        score += 10
        # incress speed
        delay -= 0.0001

        # take a high_score form file
        # # hs_file = open("highest_score_game.text", "r")
        # high_score = int(hs_file.read())
        # hs_file.close()
        # sb.clear()

        # score update
        if score > high_score:
            high_score = score

        # write new score in file
        # hs_file = open("highest_score_game.text", "w")
        # hs_file.write(str(high_score))

        # show score
        # sb.write("score: {} | heighest Score: {}".format(score, high_score))

    # snake eat own body
    for index in range(len(snake_body) - 1, 0, -1):
        x = snake_body[index - 1].xcor()
        y = snake_body[index - 1].ycor()
        snake_body[index].goto(x, y)
    if len(snake_body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].goto(x, y)
    move()
    for eat_food in snake_body:
        # if eat_food.distance(snake) < 20:
        #     game_over()
        #     time.sleep(1)
        #     eat_food.goto(0, 0)
        #     eat_food.direction = "stop"
        #     for eat_food in snake_body:
        #         eat_food.goto(1000, 1000)
        #         eat_food.ht()
        #     eat_food.clear()

        #     score = 0
        #     delay = 0.1
            # sb.clear()
            # sb.write("score: {} | heighest Score: {}".format(
            #     score, high_score))
    # time.sleep(delay)

wn.mainloop()
