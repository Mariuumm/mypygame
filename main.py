import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Catch the Shape Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

# Set up the turtle (player)
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.setheading(90)  # Face up

# Set up the shape (target)
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(-290, 290), random.randint(-290, 290))

# Initialize the score
score = 0

# Function to move the player up
def move_up():
    player.sety(player.ycor() + 20)

# Function to move the player down
def move_down():
    player.sety(player.ycor() - 20)

# Function to move the player left
def move_left():
    player.setx(player.xcor() - 20)

# Function to move the player right
def move_right():
    player.setx(player.xcor() + 20)

# Function to catch the shape
def catch_shape():
    global score
    if player.distance(target) < 20:
        # Move the shape to a new random location
        target.goto(random.randint(-290, 290), random.randint(-290, 290))
        # Increase the score
        score += 1
        print(f"Score: {score}")

# Keyboard bindings
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(catch_shape, "space")

# Main game loop
while True:
    wn.update()
