import json
import matplotlib.pyplot as plt
import numpy as np

DATA=None
LABELS = ["RANDOM",
"BACK TO FRONT",
"FRONT TO BACK",
"BACK TO FRONT GROUP 4",
"FRONT TO BACK GROUP 4",
"WINDOW MIDDLE ISLE",
"STEFFEN PERFECT",
"STEFFEN MODIFIED"]
with open('distribution_chart_data.txt') as json_file:
    DATA = json.load(json_file)

for data,label in zip(DATA,LABELS):
    plt.hist(data,alpha=0.5,label=label,density=True)
plt.legend(prop={'size': 7},loc='upper center', bbox_to_anchor=(0.5, -0.05),
           fancybox=True, shadow=True, ncol=4)
plt.savefig("ALL.png")

plt.clf()