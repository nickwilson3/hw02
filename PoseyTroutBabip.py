import matplotlib
import json
from matplotlib import pyplot as plt
import numpy as np

with open('troutstats.json', 'r') as trout:
    text = trout.read()
with open('poseystats.json', 'r') as posey:
    text1 = posey.read()
#babip for the average on balls in play
#tb for total bases

mike = json.loads(text)
busterposey = json.loads(text1)

stats = {}
stats['average on balls in play'] = mike['babip']

stats1 = {}
stats1['average on balls in play'] = busterposey['babip']

width = 0.25
x = np.arange(len(stats.keys()))
fig, ax = plt.subplots()
rect1 = ax.bar(x - width, stats.values(), width, label='Trout',color='red')
rect2 = ax.bar(x + width, stats1.values(), width, label='Posey',color='orange')

ax.set_xlabel('Statistics')
ax.set_ylabel('Result')
ax.set_xticks(x)
ax.set_xticklabels(stats.keys())
ax.legend()
plt.title("Posey vs. Trout")

plt.show()