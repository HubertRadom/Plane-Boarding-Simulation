import turtle
from State import State

class World():
    instance=None
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance=World()
        return cls.instance
    def __init__(self):
        self.passengers = []
        self.screen = turtle.Screen()
        self.screen.title("Plane")
        self.screen.bgpic("./chart.png")
        self.screen.tracer(0)
        
    def add_passenger(self,passenger):
        self.passengers.append(passenger)
    def update(self):
        self.screen.update()
    def reset(self):
        for p in self.passengers:
            p.body.clear()
        self.passengers = []
        self.screen.clear()
        self.screen.title("Plane")
        self.screen.bgpic("./chart.png")
        self.screen.tracer(0)
        self.screen.update()

    def is_corridor_blocked(self,positionX):
        for other in self.passengers:
            if positionX == other.position[0] and other.position[1] == 0:
                return True
        return False
    def is_corridor_blocked_rightside(self,passenger):
        for other in self.passengers:
            if passenger.position[0]+1 == other.position[0] and passenger.position[1] == other.position[1]:
                return True
        return False
    def is_seatmate_waiting(self,passenger):
        for other in self.passengers:
            if (passenger.position[0]-2 == other.position[0] and other.destiny[0] == passenger.destiny[0]
                and passenger.destiny[1]>0 and other.destiny[1]>0 and other.position[1]==0):
                return True
            if (passenger.position[0]-2 == other.position[0] and other.destiny[0] == passenger.destiny[0]
                and passenger.destiny[1]<0 and other.destiny[1]<0 and other.position[1]==0):
                return True
            if passenger.position[0]-1 == other.position[0] and other.position[1] == passenger.position[1]:
                return True
        return False
    def get_blocking_seatmates(self,passenger):
        seatmates=[]
        for other in self.passengers:
            if (passenger.position[0]+1 == other.position[0] and passenger.destiny[1] > 0 and other.position[1] > 0 and passenger.destiny[1] > other.position[1] or
            passenger.position[0]+1 == other.position[0] and passenger.destiny[1] < 0 and other.position[1] < 0 and passenger.destiny[1] < other.position[1]):
                seatmates.append(other)
        return seatmates
    def are_passengers_coming_back(self,passenger):
        for other in self.passengers:
            if ((passenger.position[0]+2 == other.position[0] or passenger.position[0]+3 == other.position[0] or passenger.position[0]+4 == other.position[0])
                and other.state == State.COMMING_BACK and passenger.destiny[0] != other.destiny[0]):
                return True
        return False
    def is_coming_back_seatmate(self,passenger):
        for other in self.passengers:
            if (passenger.position[0]+2 == other.position[0] and other.state == State.COMMING_BACK and passenger.destiny[0] == other.destiny[0]
                and ((passenger.destiny[1]>0 and other.destiny[1]>0) or (passenger.destiny[1]<0 and other.destiny[1]<0))):
                return True
        return False
    def is_other_shuffeling(self,passenger):
        for other in self.passengers:
            if (passenger.position[0]-1 == other.position[0] and passenger.position[1] == other.position[1] and other.state == State.SHUFFLING):
                return True
        return False
    def is_other_coming_back_down(self,passenger):
        for other in self.passengers:
            if ((passenger.position[0]+1 == other.position[0] or passenger.position[0]+2 == other.position[0]) and passenger.position[1]-1 == other.position[1]
               and other.state == State.COMMING_BACK and not (other.destiny[1]>0)):
               return True
        return False
    def is_other_coming_back_up(self,passenger):
        for other in self.passengers:
            if ((passenger.position[0]+1 == other.position[0] or passenger.position[0]+2 == other.position[0]) and passenger.position[1]+1 == other.position[1]
               and other.state == State.COMMING_BACK and not (other.destiny[1]<0)):
               return True
        return False
    def is_other_up(self,passenger):
        for other in self.passengers:
            if passenger.position[0] == other.position[0] and passenger.position[1]+1 == other.position[1]:
                return True
        return False
    def is_other_down(self,passenger):
        for other in self.passengers:
            if passenger.position[0] == other.position[0] and passenger.position[1]-1 == other.position[1]:
                return True
        return False
    def is_other_stowing_up(self,passenger):
        for other in self.passengers:
            if (passenger.position[0] == other.position[0] and passenger.destiny[0] == other.destiny[0] and other.position[1]==0 
            and other.destiny[1]<0):
                return True
        return False
    def is_other_stowing_down(self,passenger):
        for other in self.passengers:
            if (passenger.position[0] == other.position[0] and passenger.destiny[0] == other.destiny[0] and other.position[1]==0 
            and other.destiny[1]>0):
                return True
        return False
