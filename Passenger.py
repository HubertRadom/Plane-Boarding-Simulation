from enum import Enum
import turtle
import time
import random
from World import World

class State(Enum):
    GOING_TO_SEAT = 1
    SEATING = 2
    SHUFFLING = 3
    WAITING_TO_COME_BACK = 4
    COMMING_BACK=5

class Passenger():
    def __init__(self,color,destiny):
        self.body = turtle.Turtle()
        self.body.speed(0)
        self.body.shape('turtle')
        self.body.color(color)
        self.body.penup()
        self.body.goto(-285,0)
        self.destiny = destiny
        self.position=[-2,0]
        #self.state = State.GOING_TO_SEAT
        self.shuffle = False
        self.comeback = False
    def right(self):
        x = self.body.xcor()
        self.body.setx(x+30)
        self.position[0]+=1
    def left(self):
        x = self.body.xcor()
        self.body.setx(x-30)
        self.position[0]-=1
    def up(self):
        y = self.body.ycor()
        self.body.sety(y+30)
        self.position[1]+=1
    def down(self):
        y = self.body.ycor()
        self.body.sety(y-30)
        self.position[1]-=1
    def move(self):
        block = False
        if self.shuffle == True: #seat shuffling ball is going to the corridor  
            #block = False
            if self.position[1] > 0: #down
                if self.position[1] == 1:
                    for ball2 in World.get_instance().passengers:
                        if self.position[0] == ball2.position[0] and ball2.position[1] == 0:
                            block = True
                    if block == False:
                        self.down()
                else:
                    self.down()

            elif self.position[1] < 0: #up
                if self.position[1] == -1:
                    for ball2 in World.get_instance().passengers:
                        if self.position[0] == ball2.position[0] and ball2.position[1] == 0:
                            block = True
                    if block == False:
                        self.up()
                else:
                    self.up()

            elif self.position[1] == 0:
                self.right()

                self.shuffle = False
                self.comeback = True

        elif self.comeback == True: #ball is coming back to destiny X
            block = False
            for ball2 in World.get_instance().passengers:
                if self.position[0]-2 == ball2.position[0] and self.destiny[0] == ball2.destiny[0]:
                    block = True
            if block == False:
                self.left()
                self.comeback = False
        
        else:
            if self.position[0] == self.destiny[0]: #if ball is on correct X
                if self.position[1] != self.destiny[1]: #if ball isn't on destiny
                    if self.position[1] > self.destiny[1]: #should goes down
                        self.down()
                    else:                           #should goes up
                        self.up()
            else:                                   #if ball isn't on correct X
                for ball2 in World.get_instance().passengers:
                   
                    if self.position[0]+1 == self.destiny[0]: #if next X is correct
                        #if it requires seat shuffle (2 options)
                        if self.position[0]+1 == ball2.position[0] and self.destiny[1] > 0 and ball2.position[1] > 0 and self.destiny[1] > ball2.position[1]:
                            block = True
                            ball2.shuffle = True
                        if self.position[0]+1 == ball2.position[0] and self.destiny[1] < 0 and ball2.position[1] < 0 and self.destiny[1] < ball2.position[1]:
                            block = True
                            ball2.shuffle = True
                    
                    if self.position[0]+1 == ball2.position[0] and self.position[1] == ball2.position[1]: #if corridor is blocked
                        block = True
                    #if it isn't ball that caused shuffeling and should wait for coming back
                    if self.position[0]+2 == ball2.position[0] and ball2.comeback == True and self.destiny[0] != ball2.destiny[0]:
                        block = True

                if block == False:  #if corridor isn't blocked
                    self.right()