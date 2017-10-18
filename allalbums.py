import json
from collections import defaultdict
import operator

#create all-artists' profiles from all-album dictionary

with open("albums.json") as json_file:
    allalbums = json.load(json_file)

allartists = {}
artist_index = {}
score_dict = {}


def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items())

source = allalbums['artist']
artist_index = dict(sorted(list_duplicates(source)))

print(artist_index)

for artist in artist_index:
	album_list = []
	total_score = 0
	index_num = range(len(artist_index[artist]))
	for n in index_num:
		album_info = {}
		album_index = artist_index[artist][n]
		album_info['album_name'] = allalbums['album'][album_index]
		album_info['album_score'] = allalbums['score'][album_index]
		album_info['album_accolade'] = allalbums['accolade'][album_index]
		album_info['album_label'] = allalbums['label'][album_index]
		album_info['album_release'] = allalbums['released'][album_index]
		album_list.append(album_info)
		artist_r = artist.lower().replace(' ', '').lstrip('the')
		allartists[artist] = album_list
		total_score += allalbums['score'][album_index]
	average_score = total_score / len(artist_index[artist])
	score_dict[artist_r] = ["{0:.2f}".format(average_score), artist]

with open('/Users/fanjun/Desktop/twitter/allartists.json', 'w') as fp:
    json.dump(allartists, fp)

with open('/Users/fanjun/Desktop/twitter/score_dict.json', 'w') as fp:
    json.dump(score_dict, fp)



#sorted_score = sorted(score_dict.items(), key=operator.itemgetter(1), reverse = True)

#print(sorted_score)
#with open('/Users/fanjun/Desktop/twitter/allartists.json', 'w') as fp:
    #json.dump(allartists, fp)



