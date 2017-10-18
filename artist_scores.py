# load the list of tuple
# twitter_artists = ....load ....

import json
from collections import defaultdict
import operator 
import csv

artist_scores = {}

with open("score_dict.json") as json_file:
    score_dict = json.load(json_file)

with open("mention_engage.json") as json_file:
    twitter_result = json.load(json_file)

for mentioned_user in twitter_result:
	if mentioned_user in score_dict:
		score_list = [twitter_result[mentioned_user], float(score_dict[mentioned_user][0]), score_dict[mentioned_user][1]]
		artist_scores[mentioned_user] = score_list
	else: 
		print(mentioned_user)

with open('/Users/fanjun/Desktop/twitter/artist_scores.json', 'w') as fp:
    json.dump(artist_scores, fp)

out = open("/Users/fanjun/Desktop/twitter/artist_scores.csv", 'w')
# for v in artist_scores.values():
# 	print(v)
# 	out.write("%d,%d,%s\n", tuple(v))
# out.close()

writer = csv.writer(out)
for v in artist_scores.values():
	writer.writerow(v)

