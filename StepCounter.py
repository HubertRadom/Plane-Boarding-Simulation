import turtle
class StepCounter():
    def __init__(self):
        self.body = turtle.Turtle()
        self.body.speed(0)
        self.body.color("black")
        self.body.penup()
        self.body.hideturtle()
        self.body.goto(0, 260)

    def updateSteps(self,steps):
        self.body.clear()
        self.body.write("steps: "+str(steps), align = "center", font=("Courier", 24, "normal"))
    def clear(self):
        self.body.clear()
