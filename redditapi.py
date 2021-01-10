import praw
from prawcore import NotFound
from prawcore.exceptions import Forbidden
import sys


def create_connection():
    reddit = praw.Reddit(client_id='<your client_id>',
                         client_secret='<your clinet_secret>',
                         user_agent='<your user_agent>',
                         username='<your user_name>')
    return reddit


def get_subreddit(reddit):
    while True:
        u_sub = input('Type a subreddit to analyze!: ')
        try:
            subreddit = reddit.subreddits.search_by_name(u_sub, exact=True)[0]
            return subreddit
        except NotFound:
            print("Subreddit does not exist!")


def get_posts(subreddit):
    try:
        posts = set()  # use a set to clear any duplicates
        for post in subreddit.new(limit=50):
            posts.add(post)
        posts = list(posts)  # easier to work with lists
        return posts
    except Forbidden:
        print("Could not access subreddit! Quitting program.")
        sys.exit(1)
