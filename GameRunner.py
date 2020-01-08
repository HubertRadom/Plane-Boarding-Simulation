from Passenger import Passenger
from World import World
from StepCounter import StepCounter
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from orders_generation import *

class Game():
    def __init__(self, destinies):
      self.destinies = destinies
      self.number_of_passengers = len(destinies)
      self.randomColors = ["#AF88A2","#6B9EA6","#A51480","#E7233C","#50675D","#DFC6EA","#67D29B","#4DF238","#97B2E9","#6A4DD2","#A32E14","#C6C132","#4FCD5C",\
                "#CEC293","#19054E","#DE56F4","#DE5080","#C57338","#AD7D1B",]
    def play(self,should_stow):
      stepsCounter = StepCounter()
      steps=0
      stow_times =list(np.random.normal(loc=5.0,size=self.number_of_passengers)) if should_stow else [0]*self.number_of_passengers
      for i in range(self.number_of_passengers): #creating passengers
          World.get_instance().add_passenger(Passenger(random.choice(self.randomColors),self.destinies[i],i,stow_times[i]))
      while True:
        steps+=1
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
        if steps > 1000:
            raise time.sleep(9999999999999999999999999)
        #time.sleep(0.1)
      return steps

ITERATIONS=1   
def conduct_test(test,should_stow=True):
  STEPS=[]
  for i in range(ITERATIONS):
    game = Game(test[1])
    STEPS.append(game.play(should_stow))
  plt.hist(STEPS)
  plt.savefig(test[0]+".png")
  plt.clf()
##later copy below code to main

tests = [["RANDOM",random_order()],
["BACK TO FRONT",back_to_front()],
["FRONT TO BACK",front_to_back()],
["BACK TO FRONT GROUP 4",back_to_front_4()],
["FRONT TO BACK GROUP 4",front_to_back_4()],
["WINDOW MIDDLE ISLE",window_middle_isle()],
["STEFFEN PERFECT",steffen_perfect()],
"STEFFEN MODIFIED",steffen_modified()]

for test in tests:
  conduct_test(test)


no_stowing_tests = [["RANDOM NO STOWING",random_order()],
["BACK TO FRONT 4 GROUPS NO STOWING",back_to_front_4()]]

for test in no_stowing_tests:
  conduct_test(test,False)

no_shuffling_tests = [["RANDOM NO STOWING",random_without_shuffle()],
["BACK TO FRONT 4 GROUPS NO STOWING",back_to_front_4_without_shuffle()]]

for test in no_shuffling_tests:
  conduct_test(test)


