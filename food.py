from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.refresh()
        self.is_visible=True
        self.blink_blink()

    def refresh(self):
        random_x=random.randint(-250,250)
        random_y=random.randint(-250,250)
        self.goto(random_x,random_y)
    def blink_blink(self):
        if self.is_visible:
            self.hideturtle()
        else: self.showturtle()
        self.is_visible=not self.is_visible
        self.getscreen().ontimer(self.blink_blink,400)