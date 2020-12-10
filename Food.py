from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # default of Turtle class is 20,20
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.random(), random.random(), random.random())
        self.color()
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """
        refresh random location and color
        :return: None
        """
        self.color(random.random(), random.random(), random.random())
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))