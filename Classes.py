from pydraw import *


class Character:

    def __init__(self, s, x_loc, y_loc):
        self._screen = s
        self._x = x_loc
        self._y = y_loc

        # creation of the character
        self._head = Oval(screen=self._screen, x=self._x - 1, y=self._y, width=50 + 1, height=50)
        self._head.move(0, -(self._head.height() / 2))
        self._body = Rectangle(screen=self._screen, x=self._x, y=self._y, width=50, height=65)

        self._ring_1 = Rectangle(screen=self._screen, x=self._body.x(), y=self._body.y() + 30,
                                 width=self._body.width(), height=self._body.height() / 9)
        self._ring_2 = Rectangle(screen=self._screen, x=self._body.x(), y=self._body.y() + 50,
                                 width=self._body.width(), height=self._body.height() / 9)

        self._right_eye = Oval(screen=self._screen, x=self._head.x() + 10, y=self._head.y() + 10, width=5, height=7)
        self._left_eye = Oval(screen=self._screen, x=self._head.x() + 20, y=self._head.y() + 8, width=5, height=5)

        self._snout = Rectangle(screen=self._screen, x=self._head.x(), y=self._head.y() + (self._head.height() / 2),
                                width=-30, height=15)

        self._far_left_leg = Line(self._screen, self._body.x(), self._body.y() + self._body.height(),
                                  self._body.x(), self._body.y() + self._body.height() + 15)

        self._left_leg = Line(self._screen, self._body.x() + 15, self._body.y() + self._body.height(),
                              self._body.x() + 15, self._body.y() + self._body.height() + 15)

        self._right_leg = Line(self._screen, self._body.x() + self._body.width() - 15,
                               self._body.y() + self._body.height(),
                               self._body.x() + self._body.width() - 15, self._body.y() + self._body.height() + 15)

        self._far_right_leg = Line(self._screen, self._body.x() + self._body.width(),
                                   self._body.y() + self._body.height(),
                                   self._body.x() + self._body.width(), self._body.y() + self._body.height() + 15)

        self._is_left = True

        # making the characters color correct.
        body_color = Color(222, 224, 63)
        ring_color = Color(48, 171, 54)
        self._head.color(body_color)
        self._body.color(body_color)
        self._snout.color(body_color)
        self._ring_1.color(ring_color)
        self._ring_2.color(ring_color)

        # adding border around character
        border_color = Color('Black')
        self._head.border(border_color, width=2)
        self._body.border(border_color, width=2)
        self._ring_1.border(border_color, width=2)
        self._ring_2.border(border_color, width=2)
        self._snout.border(border_color, width=2)

        self._far_left_leg.thickness(2)
        self._left_leg.thickness(2)
        self._right_leg.thickness(2)
        self._far_right_leg.thickness(2)

        self._width = self._body.width() - self._snout.width()
        self._height = self._body.height() + (self._head.height() / 2)

    @property
    def x_value(self):
        if self._is_left:
            return self._head.x() + self._snout.width()
        else:
            return self._head.x()

    @x_value.setter
    def x_value(self, new_x):
        self._x = new_x

    @property
    def y_value(self):
        return self._head.y()

    @y_value.setter
    def y_value(self, new_y):
        self._y = new_y

    @property
    def width_value(self):
        return self._width

    @width_value.setter
    def width_value(self, new_width):
        self._width = new_width

    @property
    def height_value(self):
        return self._height

    @height_value.setter
    def height_value(self, new_height):
        self._height = new_height

    def move(self, x, y):
        self._head.move(x, y)
        self._body.move(x, y)
        self._ring_1.move(x, y)
        self._ring_2.move(x, y)
        self._right_eye.move(x, y)
        self._left_eye.move(x, y)
        self._snout.move(x, y)
        self._far_left_leg.move(x, y)
        self._left_leg.move(x, y)
        self._right_leg.move(x, y)
        self._far_right_leg.move(x, y)

    def moveto(self, x, y):
        self._head.moveto(x - self._snout.width() - 1, y)
        self._body.moveto(x - self._snout.width(), y + self._head.height() / 2)

        self._ring_1.moveto(self._body.x(), self._body.y() + 30)
        self._ring_2.moveto(self._body.x(), self._body.y() + 50)

        self._right_eye.moveto(self._head.x() + 10, self._head.y() + 10)
        self._left_eye.moveto(self._head.x() + 20, self._head.y() + 8)

        self._snout.moveto(self._head.x(), self._head.y() + (self._head.height() / 2))

        self._far_left_leg.moveto(self._body.x(), self._body.y() + self._body.height(),
                                  self._body.x(), self._body.y() + self._body.height() + 15)
        self._left_leg.moveto(self._body.x() + 15, self._body.y() + self._body.height(),
                              self._body.x() + 15, self._body.y() + self._body.height() + 15)
        self._right_leg.moveto(self._body.x() + self._body.width() - 15, self._body.y() + self._body.height(),
                               self._body.x() + self._body.width() - 15, self._body.y() + self._body.height() + 15)

        self._far_right_leg.moveto(self._body.x() + self._body.width(), self._body.y() + self._body.height(),
                                   self._body.x() + self._body.width(), self._body.y() + self._body.height() + 15)

    def turn_right(self):
        self._snout.moveto(self._body.x() + self._body.width() - self._snout.width(), self._snout.y())
        self._left_eye.moveto(self._head.x() + self._head.width() - 25, self._left_eye.y())
        self._right_eye.moveto(self._body.x() + self._body.width() - 15, self._right_eye.y())
        self._is_left = False

    def turn_left(self):
        self._snout.moveto(self._body.x(), self._snout.y())
        self._left_eye.moveto(self._head.x() + 20, self._left_eye.y())
        self._right_eye.moveto(self._head.x() + 10, self._right_eye.y())
        self._is_left = True

    def jump(self):
        pass


class Platform:

    def __init__(self, screen, x, y, kind):
        self._screen = screen
        self._x = x
        self._y = y
        self._kind = kind

        if kind == 'non-movable':
            self.platform = Rectangle(self._screen, self._x, self._y, 100, 20, Color('green'))

    def overlap(self, doodle):
        if self.platform.overlaps(doodle):
            return True
        return False
