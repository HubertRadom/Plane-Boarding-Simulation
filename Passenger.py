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
        if self.state == State.SHUFFLING:
            self.move_shuffle()
        elif self.state == State.COMMING_BACK:
            self.move_comming_back()
        elif self.state == State.GOING_TO_SEAT:
            self.move_to_seat()
    def move_shuffle(self):
        if self.position[1] > 0:
            if not World.get_instance().get_neighbour_cell(self,0,-1):
                self.down()
        elif self.position[1] < 0:
            if not World.get_instance().get_neighbour_cell(self,0,1):
                self.up()
        else:
            left_neighbour = World.get_instance().get_neighbour_cell(self,-1,0)
            if left_neighbour and self.position[0]< self.destiny[0]+2 and(not left_neighbour.state == State.GOING_TO_SEAT or self.position[0] == self.destiny[0]):
                right_neighbour_2 = World.get_instance().get_neighbour_cell(self,2,0)
                if not World.get_instance().get_neighbour_cell(self,1,0) and (not right_neighbour_2 or (not right_neighbour_2.state in[State.SHUFFLING,State.COMMING_BACK] or self.destiny[0]==right_neighbour_2.destiny[0])):#risky
                    self.right()
    def move_comming_back(self):
        if self.position[0] == self.destiny[0]:
            if self.position[1] == self.destiny[1]:
                self.state = State.SEATING
            elif self.position[1] < self.destiny[1]:
                self.up()
            else:
                self.down()
        else:
            left_neighbour = World.get_instance().get_neighbour_cell(self,-1,0)
            if left_neighbour and(left_neighbour.state==State.SHUFFLING or left_neighbour.destiny[0]==self.destiny[0]):
                return
            left_neighbour_2 = World.get_instance().get_neighbour_cell(self,-2,0)

            if left_neighbour_2 and self.has_similar_destiny(left_neighbour_2) and not left_neighbour_2.state == State.COMMING_BACK:
                return
            self.left()
    def move_to_seat(self):
        if self.position[0] == self.destiny[0]: #if ball is on correct X
            if self.position[1] != self.destiny[1]: #if ball isn't on destiny
                if self.stow_time > 0:
                    self.stow_time-=1
                elif self.position[1] > self.destiny[1]: #should goes down
                    self.down()
                else:                           #should goes up
                    self.up()
            else:
                self.state=State.SEATING
                for other in World.get_instance().get_shuffeled_seatmates(self):
                    other.state=State.COMMING_BACK
        else:                                   #if ball isn't on correct X                   
            block=False
            if self.position[0]+1 == self.destiny[0]: #if next X is correct
                #if it requires seat shuffle
                blocking_seatmates=World.get_instance().get_blocking_seatmates(self)
                if len(blocking_seatmates)>0:
                    block=True
                    if not World.get_instance().are_oposite_shuffling(self):
                        for s in blocking_seatmates:
                            s.state=State.SHUFFLING

                # for other in World.get_instance().get_blocking_seatmates(self) :
                #     block = True
                #     other.state = State.SHUFFLING
            right_neighbour_2 = World.get_instance().get_neighbour_cell(self,2,0)
            if (World.get_instance().get_neighbour_cell(self,1,0) or 
                (right_neighbour_2 and (right_neighbour_2.state==State.SHUFFLING or right_neighbour_2.state==State.COMMING_BACK) 
                and not self.has_similar_destiny(right_neighbour_2) )):
                block=True
        
            if block == False:  #if corridor isn't blocked
                self.right()
    def has_similar_destiny(self,other):
        return other.destiny[0] == self.destiny[0] and ((self.destiny[1]>0) == (other.destiny[1]>0))
        
        