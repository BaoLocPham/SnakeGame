from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        for position in self.starting_pos:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        """
        add segment to the snake
        :param position: position to insert new segment
        :return:
        """
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """
        extend the snake by new segment in last segment
        :return:
        """
        self.add_segment(self.segments[-1].position())

    def left(self):
        """
        turn head to left (set heading to 180deg)
        :return:
        """
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        """
        turn head to right (set heading to 0deg)
        :return:
        """
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        """
        turn head to up (set heading to 90deg)
        :return:
        """
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        """
        turn head to down (set heading to 270deg)
        :return:
        """
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move(self):
        """
        move the heading forward 20 digits, no matter what heading is
        :return:
        """
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.segments[0].forward(20)
