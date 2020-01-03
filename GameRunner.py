from Passenger import Passenger
from World import World
from StepCounter import StepCounter
import time
import random
import numpy as np
import matplotlib.pyplot as plt


class Game():
    def __init__(self, destinies):
      self.destinies = destinies
      self.number_of_passengers = len(destinies)
      self.randomColors = ["#AF88A2","#6B9EA6","#A51480","#E7233C","#50675D","#DFC6EA","#67D29B","#4DF238","#97B2E9","#6A4DD2","#A32E14","#C6C132","#4FCD5C",\
                "#CEC293","#19054E","#DE56F4","#DE5080","#C57338","#AD7D1B",]
    def play(self):
      stepsCounter = StepCounter()
      steps=0
      stow_times =list(np.random.normal(loc=5.0,size=self.number_of_passengers))
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

STEPS_forward=[]
for i in range(ITERATIONS):
  print(i)
  randomDestiny = []
  k=0
  for i in range(1, 17): #creating list of possible destinies
      for j in range(3, 0,-1):
          randomDestiny.append([i,j])
          randomDestiny.append([i,-j])

  #random.shuffle(randomDestiny)
  game = Game(randomDestiny)
  STEPS_forward.append(game.play())



plt.hist(STEPS_forward)
plt.savefig("forward.png")
plt.clf()


STEPS_backwards=[]
for i in range(ITERATIONS):
  print(i)
  randomDestiny = []
  k=0
  for i in range(16, 0,-1): #creating list of possible destinies
      for j in range(3, 0,-1):
          randomDestiny.append([i,j])
          randomDestiny.append([i,-j])

  #random.shuffle(randomDestiny)
  game = Game(randomDestiny)
  STEPS_backwards.append(game.play())



plt.hist(STEPS_backwards)
plt.savefig("backward.png")
plt.clf()

