"""
A robot capable of four actions: moving forward one step, turning right, turning
left, and reporting its location.

>>> go_bot = Robot()
>>> print go_bot.move_one().turn_right().move_one().move_one().say_where()
I am located at [1, -2].

>>> oh_no_bot = Robot()
>>> print oh_no_bot.move_one().turn_right().move_one().turn_right().move_one().turn_right().move_one().say_where()
I am located at [0, 0].

"""


class Robot(object):

    def __init__(self):

        self.orientation = 0
        self.location = [0, 0]

    def move_one(self):

        if self.orientation == 100:
            self.orientation = 0
        if self.orientation == -25:
            self.orientation = 75

        # forward
        if self.orientation == 0:
            self.location[0] += 1

        # up
        elif self.orientation == 25:
            self.location[1] += 1

        # backward
        elif self.orientation == 50:
            self.location[0] -= 1

        # down
        elif self.orientation == 75:
            self.location[1] -= 1

        return self

    def turn_left(self):

        self.orientation += 25
        return self

    def turn_right(self):

        self.orientation -= 25
        return self

    def say_where(self):

        return "I am located at {here}.".format(here=self.location)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\nALL TESTS PASSED. BLEEP BLOOP!! <3\n"
