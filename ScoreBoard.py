from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("HighScore.txt", "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(x=0, y=270)
        self.color('white')
        # hide turtle
        self.hideturtle()
        self.score = 0
        self.print_score()

    def print_score(self):
        """
        print score to the screen
        :return:
        """
        self.clear()
        self.write(f"Score: {self.score}| HighScore: {self.high_score}", align='center', font=("Arial", 20, "bold"))

    def print_final_score(self):
        """
        print final score to middle screen
        :return:
        """
        self.clear()
        self.goto(0, 0)
        self.print_score()
        with open("HighScore.txt", "w") as file:
            file.write(str(self.high_score))

    def increase_score(self):
        """
        increase score
        :return:
        """
        self.score += 1
        if self.score> self.high_score:
            self.high_score = self.score
        self.print_score()