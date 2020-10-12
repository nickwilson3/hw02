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


stats2 = {}
stats2['on base %'] = mike['obp']
stats2['slugging &'] = mike['slg']
stats2['on base plus slugging %'] = mike['ops']
labels = 'OBP', 'SLG', 'OPS'

fig1,ax1 = plt.subplots()
ax1.pie(stats2.values(),labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.title('Mike Trout OPS')

plt.show()




