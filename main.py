from GameRunner import Game
from orders_generation import *
import matplotlib.pyplot as plt
   
def conduct_test(test,visualise,should_stow=True):
  print("Starting test: "+test[0])
  STEPS=[]
  for i in range(ITERATIONS):
    print("Iteration: "+str(i+1)+"/"+str(ITERATIONS))
    game = Game(test[1],visualise)
    STEPS.append(game.play(should_stow))
  plt.hist(STEPS,5,density=True)
  plt.savefig(test[0]+".png")
  plt.clf()

ITERATIONS=10
VISUALISE=False

tests = [["RANDOM",random_order()],
["BACK TO FRONT",back_to_front()],
["FRONT TO BACK",front_to_back()],
["BACK TO FRONT GROUP 4",back_to_front_4()],
["FRONT TO BACK GROUP 4",front_to_back_4()],
["WINDOW MIDDLE ISLE",window_middle_isle()],
["STEFFEN PERFECT",steffen_perfect()],
["STEFFEN MODIFIED",steffen_modified()]]

for test in tests:
  conduct_test(test,VISUALISE)


no_stowing_tests = [["RANDOM NO STOWING",random_order()],
["BACK TO FRONT 4 GROUPS NO STOWING",back_to_front_4()]]

for test in no_stowing_tests:
  conduct_test(test,VISUALISE,False)

no_shuffling_tests = [["RANDOM NO STOWING",random_without_shuffle()],
["BACK TO FRONT 4 GROUPS NO STOWING",back_to_front_4_without_shuffle()]]

for test in no_shuffling_tests:
  conduct_test(test,VISUALISE)


