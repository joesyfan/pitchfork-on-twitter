import json
from collections import defaultdict
import operator
import csv

# count mentioned-users' engagement

with open("allresult.json") as json_file:
    tweet_d = json.load(json_file)

mention_engage = defaultdict(int)

for t in tweet_d:
	for mention in tweet_d[t][1]:
		engagement = tweet_d[t][2] + tweet_d[t][3]
		mention_name = mention['name']
		#mention_name = mention_name.lower().replace(' ', '').strip('.com').strip('official').lstrip('the')
		mention_engage[mention_name] += engagement

# out = open("/Users/fanjun/Desktop/twitter/artist_scores.csv", 'w')
# for n, count in mention_engage.items():
# 	out.write(n + ", " + str(count) + "\n")

# out.close
with open('/Users/fanjun/Desktop/twitter/mention_engage_lower.json', 'w') as fp:
    json.dump(mention_engage, fp)



#sorted_engage = sorted(mention_engage.items(), key=operator.itemgetter(1), reverse = True)

#print(sorted_engage[:200])