from turtle import Turtle
SCORE_POSITION=(-10,260)

def draw_fence():
    fence=Turtle()
    fence.color("white")
    fence.hideturtle()
    fence.penup()
    fence.goto(-290, -290)
    fence.pendown()
    fence.goto(-290,250)
    fence.goto(290,250)
    fence.goto(290,-290)
    fence.goto(-290,-290)



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        draw_fence()
        self.cur_score=0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.write_score()

    def fence(self):
        self.goto(-280,-280)
        self.pendown()
        self.setheading(0)
        for i in range(4):
            self.forward(560)
            self.left(90)
        self.penup()
    def write_score(self):
        self.write(f"Score: {self.cur_score}", False, "center", ('Arial', 18, 'normal'))
    def update_core(self):
        self.cur_score+=1
        self.clear()
        self.write_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"Center",('Arial', 24, 'normal'))

