import json
from collections import defaultdict
import operator

#create all-artists' profiles from all-album dictionary

with open("allartists.json") as json_file:
    allartists = json.load(json_file)

score_dict = []

for artist in allartists:
	score_dict[artist] = int(allartists[artist][-1])

sorted_score = sorted(score_dict.items(), key=operator.itemgetter(1), reverse = True)

print(sorted_score)