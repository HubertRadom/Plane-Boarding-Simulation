from GameRunner import Game
from orders_generation import *
import matplotlib.pyplot as plt


   
def conduct_test(test,visualise,should_stow=True,stowing_mean=5.0):
  print("Starting test: "+test[0])
  STEPS=[]
  for i in range(ITERATIONS):
    print("Iteration: "+str(i+1)+"/"+str(ITERATIONS))
    game = Game(test[1](),visualise,stowing_mean)
    STEPS.append(game.play(should_stow))
  plt.hist(STEPS,5,density=True)
  plt.title('Mean: '+str(sum(STEPS)/len(STEPS)))
  plt.savefig(test[0]+".png")
  plt.clf()
  return STEPS

ITERATIONS=100
VISUALISE=False

tests = [   
["RANDOM",random_order],
["BACK TO FRONT",back_to_front],
["FRONT TO BACK",front_to_back],
["BACK TO FRONT GROUP 4",back_to_front_4],
["FRONT TO BACK GROUP 4",front_to_back_4],
["WINDOW MIDDLE ISLE",window_middle_isle],
["STEFFEN PERFECT",steffen_perfect],
["STEFFEN MODIFIED",steffen_modified]]

basicTestHistogramData =[]
basicTestLabels = []

for test in tests:
  basicTestHistogramData.append(conduct_test(test,VISUALISE))
  basicTestLabels.append(test[0])


fig = plt.figure()
ax = plt.subplot(111)
ax.hist(basicTestHistogramData,5,density=True,label=basicTestLabels)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(prop={'size': 7},loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=4)
plt.savefig("allHistogram.png")
plt.clf()


no_stowing_tests = [["RANDOM NO STOWING",random_order],
["BACK TO FRONT 4 GROUPS NO STOWING",back_to_front_4]]

for test in no_stowing_tests:
  conduct_test(test,VISUALISE,False)

no_shuffling_tests = [["RANDOM NO SHUFFLE",random_without_shuffle],
["BACK TO FRONT 4 GROUPS NO SHUFFLE",back_to_front_4_without_shuffle]]

for mean in range(5,56,5):
    random_n_s = no_shuffling_tests[0].copy()
    random_n_s[0]=random_n_s[0]+" "+str(mean)
    conduct_test(random_n_s,VISUALISE,True,mean)
    btf4_n_s = no_shuffling_tests[1].copy()
    btf4_n_s[0]=btf4_n_s[0]+" "+str(mean)
    conduct_test(btf4_n_s,VISUALISE,True,mean)
