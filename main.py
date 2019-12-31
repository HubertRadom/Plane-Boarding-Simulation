import turtle
import time
import random
from World import World
from Passenger import Passenger
from StepCounter import StepCounter


wn = turtle.Screen()
wn.title("Plane")
wn.bgpic("./chart.png")
wn.tracer(0)

#list of some random colors xD
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

for i in range(96): #creating passengers
    destiny = random.choice(randomDestiny)
    randomDestiny.remove(destiny)
    World.get_instance().add_passenger(Passenger(random.choice(randomColors),destiny,i))


#Pen
stepsCounter = StepCounter()
    

# Main game loop
steps=0
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
        wn.update()
        break
    time.sleep(0.1)
