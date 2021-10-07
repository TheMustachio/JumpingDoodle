from pydraw import *
# import datetime
from Classes import Character, Platform

# setup
screen = Screen(600, 800, 'Doodle Jump')
Medici_Ivory = Color(243, 233, 215)

# background
screen.color(Medici_Ivory)
screen.grid(rows=30, cols=30, helpers=False)

doodle = Character(screen, screen.width() / 2, screen.height() / 2)
doodle.alive = True
doodle.horizontal_vector = 0
doodle.vertical_vector = -10


def fall():
    doodle.move(0, doodle.vertical_vector)
    if doodle.vertical_vector <= 10:
        doodle.vertical_vector += 1


plat = Platform(screen, screen.width()/2, 3*screen.height()/4, 'non-movable')


def check_game():
    if doodle.alive:
        if doodle.y_value > screen.height():
            doodle.alive = False


# key inputs
def keydown(key):
    global running
    if key == 'left':
        doodle.horizontal_vector = -15
        doodle.turn_left()

    if key == 'right':
        doodle.horizontal_vector = 15
        doodle.turn_right()

    if key == 'space':
        doodle.vertical_vector = -10
    if key == 'q':
        running = False


def keyup(key):
    if key == 'left':
        doodle.horizontal_vector = 0
    if key == 'right':
        doodle.horizontal_vector = 0


# run method
running = True
while running:
    # checking to see if the game will continue going
    check_game()

    if doodle.alive:
        fall()
        doodle.move(doodle.horizontal_vector, 0)

        if doodle.x_value <= 0:
            doodle.moveto(screen.width() - doodle.width_value - 10, doodle.y_value)

        if doodle.x_value + doodle.width_value >= screen.width():
            doodle.moveto(-25, doodle.y_value)
            doodle.turn_right()

    # this updates the screen for any movement
    screen.update()
    # this listens for any inputs from the user
    screen.listen()
    # this is to slow it down to 60 fps
    screen.sleep(1 / 60)

print('ending program')

screen.exit()
