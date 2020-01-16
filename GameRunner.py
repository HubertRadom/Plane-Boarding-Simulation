from Passenger import Passenger
from World import World
from StepCounter import StepCounter
import time
import random
import numpy as np

class Game():
    def __init__(self, destinies,visualise,stowing_mean):
      self.destinies = destinies
      self.number_of_passengers = len(destinies)
      self.randomColors = ["#AF88A2","#6B9EA6","#A51480","#E7233C","#50675D","#DFC6EA","#67D29B","#4DF238","#97B2E9","#6A4DD2","#A32E14","#C6C132","#4FCD5C",\
                "#CEC293","#19054E","#DE56F4","#DE5080","#C57338","#AD7D1B",]
      self.visualise = visualise
      self.stowing_mean = stowing_mean
    def play(self,should_stow):
      stepsCounter = StepCounter()
      steps=0
      stow_times =list(np.random.normal(loc=self.stowing_mean,size=self.number_of_passengers)) if should_stow else [0]*self.number_of_passengers
      for i in range(self.number_of_passengers): #creating passengers
          World.get_instance().add_passenger(Passenger(random.choice(self.randomColors),self.destinies[i],i,stow_times[i]))
      while True:
        steps+=1
        if self.visualise:
          World.get_instance().update()
        stepsCounter.updateSteps(steps)
        for passenger in World.get_instance().passengers:
            passenger.move()
        #end of symulation
        end = True
        for ball in World.get_instance().passengers:
            if ball.position != ball.destiny:
                end = False
        if end == True:
            World.get_instance().reset()
            stepsCounter.clear()
            World.get_instance().update()
            break
        #time.sleep(0.2)
      return steps
