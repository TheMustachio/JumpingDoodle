from pydraw import *


class Character:

    def __init__(self, s, x_loc, y_loc):
        self.screen = s
        self.x = x_loc
        self.y = y_loc

        # creation of the character
        self.head = Oval(screen=self.screen, x=self.x - 1, y=self.y, width=50 + 1, height=50)
        self.head.move(0, -(self.head.height() / 2))
        self.body = Rectangle(screen=self.screen, x=self.x, y=self.y, width=50, height=65)

        self.ring_1 = Rectangle(screen=self.screen, x=self.body.x(), y=self.body.y() + 30,
                                width=self.body.width(), height=self.body.height() / 9)
        self.ring_2 = Rectangle(screen=self.screen, x=self.body.x(), y=self.body.y() + 50,
                                width=self.body.width(), height=self.body.height() / 9)

        self.right_eye = Oval(screen=self.screen, x=self.head.x() + 10, y=self.head.y() + 10, width=5, height=7)
        self.left_eye = Oval(screen=self.screen, x=self.head.x() + 20, y=self.head.y() + 8, width=5, height=5)

        self.snout = Rectangle(screen=self.screen, x=self.head.x(), y=self.head.y() + (self.head.height() / 2),
                               width=-30, height=15)

        self.far_left_leg = Line(self.screen, self.body.x(), self.body.y() + self.body.height(),
                                 self.body.x(), self.body.y() + self.body.height() + 15)

        self.left_leg = Line(self.screen, self.body.x() + 15, self.body.y() + self.body.height(),
                             self.body.x() + 15, self.body.y() + self.body.height() + 15)

        self.right_leg = Line(self.screen, self.body.x() + self.body.width() - 15, self.body.y() + self.body.height(),
                              self.body.x() + self.body.width() - 15, self.body.y() + self.body.height() + 15)

        self.far_right_leg = Line(self.screen, self.body.x() + self.body.width(),
                                  self.body.y() + self.body.height(),
                                  self.body.x() + self.body.width(), self.body.y() + self.body.height() + 15)

        self.is_left = True
        self.is_moving = False

        # making the characters color correct.
        body_color = Color(222, 224, 63)
        ring_color = Color(48, 171, 54)
        self.head.color(body_color)
        self.body.color(body_color)
        self.snout.color(body_color)
        self.ring_1.color(ring_color)
        self.ring_2.color(ring_color)

        # adding border around character
        border_color = Color('Black')
        self.head.border(border_color, width=2)
        self.body.border(border_color, width=2)
        self.ring_1.border(border_color, width=2)
        self.ring_2.border(border_color, width=2)
        self.snout.border(border_color, width=2)

        self.far_left_leg.thickness(2)
        self.left_leg.thickness(2)
        self.right_leg.thickness(2)
        self.far_right_leg.thickness(2)

    def get_x(self):
        if self.is_left:
            return self.head.x() + self.snout.width()
        else:
            return self.head.x()

    def get_y(self):
        return self.head.y()

    def get_width(self):
        return self.body.width() - self.snout.width()

    def get_height(self):
        return self.body.height() + (self.head.height() / 2)

    def move(self, x, y):
        self.head.move(x, y)
        self.body.move(x, y)
        self.ring_1.move(x, y)
        self.ring_2.move(x, y)
        self.right_eye.move(x, y)
        self.left_eye.move(x, y)
        self.snout.move(x, y)
        self.far_left_leg.move(x, y)
        self.left_leg.move(x, y)
        self.right_leg.move(x, y)
        self.far_right_leg.move(x, y)

    def moveto(self, x, y):
        self.head.moveto(x - self.snout.width() - 1, y)
        self.body.moveto(x - self.snout.width(), y + self.head.height() / 2)

        self.ring_1.moveto(self.body.x(), self.body.y() + 30)
        self.ring_2.moveto(self.body.x(), self.body.y() + 50)

        self.right_eye.moveto(self.head.x() + 10, self.head.y() + 10)
        self.left_eye.moveto(self.head.x() + 20, self.head.y() + 8)

        self.snout.moveto(self.head.x(), self.head.y() + (self.head.height() / 2))

        self.far_left_leg.moveto(self.body.x(), self.body.y() + self.body.height(),
                                 self.body.x(), self.body.y() + self.body.height() + 15)
        self.left_leg.moveto(self.body.x() + 15, self.body.y() + self.body.height(),
                             self.body.x() + 15, self.body.y() + self.body.height() + 15)
        self.right_leg.moveto(self.body.x() + self.body.width() - 15, self.body.y() + self.body.height(),
                              self.body.x() + self.body.width() - 15, self.body.y() + self.body.height() + 15)

        self.far_right_leg.moveto(self.body.x() + self.body.width(), self.body.y() + self.body.height(),
                                  self.body.x() + self.body.width(), self.body.y() + self.body.height() + 15)

    def turn_right(self):
        self.snout.moveto(self.body.x() + self.body.width() - self.snout.width(), self.snout.y())
        self.left_eye.moveto(self.head.x() + self.head.width() - 25, self.left_eye.y())
        self.right_eye.moveto(self.body.x() + self.body.width() - 15, self.right_eye.y())
        self.is_left = False

    def turn_left(self):
        self.snout.moveto(self.body.x(), self.snout.y())
        self.left_eye.moveto(self.head.x() + 20, self.left_eye.y())
        self.right_eye.moveto(self.head.x() + 10, self.right_eye.y())
        self.is_left = True

    def moving(self):
        return self.is_moving

    def change_moving(self, boolean):
        self.is_moving = boolean
