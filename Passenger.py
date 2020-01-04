import turtle
import time
import random
from World import World
from State import State

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
        self.state = State.GOING_TO_SEAT
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
        if self.state == State.SHUFFLING: #seat shuffling ball is going to the corridor  
            if self.position[1] > 0: #down
                if self.position[1] == 1:
                    if not World.get_instance().is_corridor_blocked(self.position[0]) and not World.get_instance().is_other_coming_back_down(self):
                        self.down()
                elif not World.get_instance().is_other_down(self) and not World.get_instance().is_other_stowing_down(self):
                    self.down()

            elif self.position[1] < 0: #up
                if self.position[1] == -1:
                    if not World.get_instance().is_corridor_blocked(self.position[0]) and not World.get_instance().is_other_coming_back_up(self):
                        self.up()
                elif not World.get_instance().is_other_up(self) and not World.get_instance().is_other_stowing_up(self):
                    self.up()

            elif self.position[1] == 0:
                if (World.get_instance().is_corridor_blocked_rightside(self) or World.get_instance().are_passengers_coming_back(self)): 
                    block = True
                if block == False:  #if corridor isn't blocked
                    self.right()
                    self.state = State.COMMING_BACK

        elif self.state == State.COMMING_BACK: #ball is coming back to destiny X
            if (World.get_instance().is_other_shuffeling(self)) and not (World.get_instance().is_corridor_blocked_rightside(self) 
                and not World.get_instance().are_passengers_coming_back(self)):
                self.right()
            elif not World.get_instance().is_seatmate_waiting(self):
                if self.position[0]-2 == self.destiny[0]:
                    self.left()
                else:
                    self.left()
                    self.state = State.GOING_TO_SEAT
        
        else:
            if self.position[0] == self.destiny[0]: #if ball is on correct X
                if self.position[1] != self.destiny[1]: #if ball isn't on destiny
                    if self.stow_time > 0:
                        self.body.shape('square')
                        self.stow_time-=1
                    elif self.position[1] > self.destiny[1]: #should goes down
                        self.body.shape('turtle')
                        self.down()
                    else:                           #should goes up
                        self.body.shape('turtle')
                        self.up()
            else:                                   #if ball isn't on correct X                   
                if self.position[0]+1 == self.destiny[0]: #if next X is correct
                    #if it requires seat shuffle
                    for other in World.get_instance().get_blocking_seatmates(self):
                        block = True
                        other.state = State.SHUFFLING

                #if it isn't ball that caused shuffeling and should wait for coming back
                if (World.get_instance().is_corridor_blocked_rightside(self) or 
                    (World.get_instance().are_passengers_coming_back(self) and not World.get_instance().is_coming_back_seatmate(self))):
                    block = True

                if block == False:  #if corridor isn't blocked
                    self.right()
