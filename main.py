import turtle
import time
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgpic("C:\\Users\\Hubert\\Desktop\\chart.png")
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

#Ball
ballList = [] #list of turtles

for i in range(96): #creating passengers
    ball = turtle.Turtle()
    ball.speed(0)
    #ball.shape('square')
    #ball.color('black')
    ball.shape("turtle")
    ball.color(random.choice(randomColors))
    ball.penup()
    ball.goto(-285, 0)
    ball.destiny = random.choice(randomDestiny)
    randomDestiny.remove(ball.destiny)
    ball.position = [-2,0] #position X,Y
    ball.shuffle = False
    ball.comeback = False
    ballList.append(ball)


#Pen
pen = turtle.Turtle() #steps counter
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("steps: 0", align = "center", font=("Courier", 24, "normal"))

#Move
def right(ball):
    x = ball.xcor()
    ball.setx(x+30)
    ball.position[0]+=1
def left(ball):
    x = ball.xcor()
    ball.setx(x-30)
    ball.position[0]-=1
def up(ball):
    y = ball.ycor()
    ball.sety(y+30)
    ball.position[1]+=1
def down(ball):
    y = ball.ycor()
    ball.sety(y-30)
    ball.position[1]-=1
    

# Main game loop
steps=0
block=False
while True:
    wn.update()
    for ball in ballList:
        block = False
        if ball.shuffle == True: #seat shuffling ball is going to the corridor  
            #block = False
            if ball.position[1] > 0: #down
                if ball.position[1] == 1:
                    for ball2 in ballList:
                        if ball.position[0] == ball2.position[0] and ball2.position[1] == 0:
                            block = True
                    if block == False:
                        down(ball)
                else:
                    down(ball)

            if ball.position[1] < 0: #up
                if ball.position[1] == -1:
                    for ball2 in ballList:
                        if ball.position[0] == ball2.position[0] and ball2.position[1] == 0:
                            block = True
                    if block == False:
                        up(ball)
                else:
                    up(ball)

            elif ball.position[1] == 0:
                right(ball)

                ball.shuffle = False
                ball.comeback = True

        elif ball.comeback == True: #ball is coming back to destiny X
            block = False
            for ball2 in ballList:
                if ball.position[0]-2 == ball2.position[0] and ball.destiny[0] == ball2.destiny[0]:
                    block = True
            if block == False:
                left(ball)
                ball.comeback = False
        
        else:
            if ball.position[0] == ball.destiny[0]: #if ball is on correct X
                if ball.position[1] != ball.destiny[1]: #if ball isn't on destiny
                    if ball.position[1] > ball.destiny[1]: #should goes down
                        down(ball)
                    else:                           #should goes up
                        up(ball)
            else:                                   #if ball isn't on correct X
                for ball2 in ballList:
                   
                    if ball.position[0]+1 == ball.destiny[0]: #if next X is correct
                        #if it requires seat shuffle (2 options)
                        if ball.position[0]+1 == ball2.position[0] and ball.destiny[1] > 0 and ball2.position[1] > 0 and ball.destiny[1] > ball2.position[1]:
                            block = True
                            ball2.shuffle = True
                        if ball.position[0]+1 == ball2.position[0] and ball.destiny[1] < 0 and ball2.position[1] < 0 and ball.destiny[1] < ball2.position[1]:
                            block = True
                            ball2.shuffle = True
                    
                    if ball.position[0]+1 == ball2.position[0] and ball.position[1] == ball2.position[1]: #if corridor is blocked
                        block = True
                    #if it isn't ball that caused shuffeling and should wait for coming back
                    if ball.position[0]+2 == ball2.position[0] and ball2.comeback == True and ball.destiny[0] != ball2.destiny[0]:
                        block = True

                if block == False:  #if corridor isn't blocked
                    right(ball)
                block = False


    pen.clear()
    steps+=1
    pen.write("steps: {}".format(steps), align = "center", font=("Courier", 50, "normal"))
    time.sleep(0.1)
    #print("=====================================")
    #for ball in ballList:
    #    print(ball.position, ball.destiny, ball.position==ball.destiny, ball.xcor(), ball.ycor())

    #end of symulation
    end = True
    for ball in ballList:
        if ball.position != ball.destiny:
            end = False
    if end == True:
        wn.update()
        break
