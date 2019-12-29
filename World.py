import turtle

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