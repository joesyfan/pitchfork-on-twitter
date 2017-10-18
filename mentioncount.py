import json
from collections import defaultdict
import operator

# count how many times a user has been mentioned by Pitchfork 

with open("allresult.json") as json_file:
    tweet_d = json.load(json_file)

mention_count = defaultdict(int)

for t in tweet_d:
	for mention in tweet_d[t][1]:
		mention_name = mention['name']
		mention_count[mention_name] += 1

with open('/Users/fanjun/Desktop/twitter/mention_count.json', 'w') as fp:
    json.dump(mention_count, fp)



sorted_mentioncount = sorted(mention_count.items(), key=operator.itemgetter(1), reverse = True)

print(sorted_mentioncount[:100])