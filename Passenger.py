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
    def __init__(self,color,destiny,id,stow_time):
        self.id=id
        self.body = turtle.Turtle()
        self.body.speed(0)
        self.body.shape('turtle')
        self.body.color(color)
        self.body.penup()
        self.body.goto(-285,0)
        self.destiny = destiny
        self.position=[-2,0]
        self.stow_time = stow_time
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
                    if not World.get_instance().is_corridor_blocked(self.position[0]):
                        self.down()
                else:
                    self.down()

            elif self.position[1] < 0: #up
                if self.position[1] == -1:
                    if not World.get_instance().is_corridor_blocked(self.position[0]):
                        self.up()
                else:
                    self.up()

            elif self.position[1] == 0:
                self.right()

                self.shuffle = False
                self.comeback = True

        elif self.comeback == True: #ball is coming back to destiny X
            if not World.get_instance().is_seatmate_waiting(self):
                self.left()
                self.comeback = False
        
        else:
            if self.position[0] == self.destiny[0]: #if ball is on correct X
                if self.position[1] != self.destiny[1]: #if ball isn't on destiny
                    if self.stow_time > 0:
                        self.stow_time-=1
                    elif self.position[1] > self.destiny[1]: #should goes down
                        self.down()
                    else:                           #should goes up
                        self.up()
            else:                                   #if ball isn't on correct X                   
                if self.position[0]+1 == self.destiny[0]: #if next X is correct
                    #if it requires seat shuffle
                    for other in World.get_instance().get_blocking_seatmates(self):
                        block = True
                        other.shuffle = True
                
                if (World.get_instance().is_corridor_blocked_rightside(self) or 
                    World.get_instance().are_passengers_coming_back(self)):#if it isn't ball that caused shuffeling and should wait for coming back
                    block = True

                if block == False:  #if corridor isn't blocked
                    self.right()