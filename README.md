<a ref="http://joesyfan.com/pitchfork">pitchfork-on-twitter</a>

Pitchfork on Twitter is a quantitative user research project that explores Pitchfork's reviewer scores of 21447 indie music albums in the past ten years and around 3200 official tweets using Python, Tableau and D3 plus. This project was conducted in Spring 2016.

Who are the most popular mentioned-users and artists on Pitchfork's official twitter account? Are these artists also Pitchforks’ favorites? Simply put, do Pitchfork fans' social media presence and music opinions really get affected by this tiny web outfit? Apart from answering these questions, I also visualized Pitchfork's twitter network, which demonstrates how the artists, record labels, music festivals, and even politicians get connected together in this online indie music world.


DATASETS
#1 Pitchfork's reviewer scores

As the most influential tastemaker on the music scene, Pitchfork offers a valuable dataset that demonstrates the indie music trends from the perspective of a professional critic. I came across Neal S. Grantham's Pitchfork album scores and accolade dataset on Github. In Neal's analysis, he did a good job demonstrating Pitchfork’s scoring system, and being skeptical about its reviewers. Discussing reviewers’ authenticity is one angle of measuring the website; finding out what its users are talking about is equally interesting and meaningful way to review the indie music world. So I decided to put it together with social media and find out more from it. 

I used the “Albums” table in Neal's dataset, which includes album’s id (unique album identifier assigned by Pitchfork), name of the album, name of the album’s artist, name of the label that produced the album, year the album was released, name of the album’s Pitchfork reviewer, score given to the album by reviewers (0.0 to 10.0 in increments of 0.1), accolade (“Best New Music” or “Best New Reissue”), review published date, and URL of Pitchfork’s review. 21447 albums are described in the dataset, and the file is updated to Jan. 16, 2016. 

Based on it, I created an artist dictionary by assigning albums’ information to each artist. And then I calculated the mean value of all the albums scores received by each artist.

 

#2 Tweets published on Pitchfork’s Twitter official account

Using Twitter’s Rest API, I grabbed tweets’ profiles from Pitchfork’s twitter timeline on 162 pages. There are around 3200 tweets in all, dated from March 3, 2016 to May 26, 2016. Each tweet’s profile includes the tweet’s id, text, mentioned-users, retweet-number, and favorite-number. I add numbers of favorited & retweet together as an engagement score for every tweet.

http://joesyfan.com/pitchfork
