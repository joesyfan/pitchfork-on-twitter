import json
from collections import defaultdict
import operator
import csv

# Format connection pairs into Html souce code

with open("mentionlist.json") as json_file:
    mentionlist = json.load(json_file)

with open("mention_engage_upper.json") as json_file:
    engagement = json.load(json_file)

connect_degree = defaultdict(int)

mentioned = []
for pair in mentionlist:
	mentioned.append(pair["destination"])
	mentioned.append(pair["source"])


# count connection degrees

for user in mentioned:
	connect_degree[user] += 1

# with open('/Users/fanjun/Desktop/twitter/connect_degree.json', 'w') as fp:
#     json.dump(connect_degree, fp)

# create a dictionary that 
degree_engage = {}
for n in engagement:
 	if n in connect_degree:
 		degree_engage[n] = [connect_degree[n], engagement[n]]
histo = defaultdict(int)
for d in degree_engage:
	degree = degree_engage[d][0]
	histo[degree] += 1

for h in histo:
	print(str(h) + '\t' + str(histo[h])

