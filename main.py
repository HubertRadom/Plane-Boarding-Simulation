import turtle
import time
import random
from World import World
from Passenger import Passenger
from StepCounter import StepCounter
import numpy as np

number_of_passengers = 96
#list of some random colors
randomColors = ["#AF88A2","#6B9EA6","#A51480","#E7233C","#50675D","#DFC6EA","#67D29B","#4DF238","#97B2E9","#6A4DD2","#A32E14","#C6C132","#4FCD5C",\
                "#CEC293","#19054E","#DE56F4","#DE5080","#C57338","#AD7D1B",]
randomDestiny = []
k=0
for i in range(1, 17): #creating list of possible destinies
    for j in range(-3, 4):
        if j!=0:
            randomDestiny.append([])
            randomDestiny[k].append(i)
            randomDestiny[k].append(j)
            k+=1
stow_times =list(np.random.normal(loc=5.0,size=number_of_passengers))
for i in range(number_of_passengers): #creating passengers
    destiny = random.choice(randomDestiny)
    randomDestiny.remove(destiny)
    World.get_instance().add_passenger(Passenger(random.choice(randomColors),destiny,i,stow_times[i]))


#Steps Counter
stepsCounter = StepCounter()
    

# Main game loop
steps=0
while True:
    steps+=1
    print(steps)
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
        World.get_instance().update()
        break
    if steps > 1000:
        raise time.sleep(9999999999999999999999999)
    #time.sleep(0.1)
