# Subreddit Sentiment Analyzer -
Analyze the sentiment of subreddits using this Python script! This looks through the titles of posts in a subreddit and categorizes them as being
postitive, negative, or neutral.

# Methodology
Using the Reddit API, this program looks through the 50 newest posts in a subreddit and labels their titles as positive, negative, or neutral.
To do this, I am using the pretrained VADER model from NLTK. VADER returns an analysis of a sentence/article containing a positive, negative, 
neutral, (all from 0 - 1) and compound score (from -1 to 1). Any title that gets a compound score above 0.2 is labeled as positive. Any title that 
gets a compound score below -0.2 are labeled as negative. The rest of the titles are labeled as neutral. Finally, the program returns the percentages
of positive, negative, and neutral titles in the subreddit.

# Creation Process
First, I got familiar with the data and methodology within a Google Colab Notebook. Once I had explored this enough, I adapted the code to a python
project. Redditapi.py contains functions that can be used to access the Reddit API, and to get posts from a subreddit. Sentiment.py contains functions
that can be used to analyze the posts and to display the results.

# Future Work
Instead of just analyzing the titles of posts, the sentiment analysis may be expanded to look at the top comments within a post. Instead of sorting by
new, it may be more accurate to sort by another label (e.g. hot or trending). The VADER model is not trained specifically to this purpose. It may be 
better to train my own model. I also would like some different kinds of sentiment analysis (e.g. racism or fake news). Also this is going to be made to 
a web app.
