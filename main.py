from pydraw import *
import datetime
from Classes import Character

# setup
screen = Screen(600, 800, 'Doodle Jump')
Medici_Ivory = Color(243, 233, 215)

# background
screen.color(Medici_Ivory)
screen.grid(rows=30, cols=30, helpers=False)


# character movement
def move(velocity, direction):
    print('the character will move ' + str(direction) + ' for ' + str(velocity))


def character(x, y):
    x = screen.width() / 2
    y = screen.height() / 2
    return Character(screen, x, y)


# key inputs
def keydown(key):
    global running
    x_vector = 15
    if key == 'left':
        doodle.move(-x_vector, 0)
        doodle.turn_left()

        if doodle.get_x() <= 0:
            doodle.moveto(screen.width() - doodle.get_width() - 10, doodle.get_y())

    if key == 'right':
        doodle.move(x_vector, 0)
        doodle.turn_right()

        if doodle.get_x() + doodle.get_width() >= screen.width():
            doodle.moveto(-25, doodle.get_y())

        doodle.turn_right()
    if key == 'q':
        running = False


doodle = character(screen.width() / 2, screen.height() / 2)
# run method
running = True
while running:
    # this updates the screen for any movement
    screen.update()
    # this listens for any inputs from the user
    screen.listen()
    # this is to slow it down to 60 fps
    screen.sleep(1 / 60)

print('ending program')

file = open('scoreboard.txt')
for i in range(2):
    print(file.readline())

screen.exit()
