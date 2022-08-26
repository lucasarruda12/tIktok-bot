import praw
from credentials import *
import os

reddit = praw.Reddit(
    client_id = client_id, 
    client_secret = client_secret, 
    username = username, 
    password =  password, 
    user_agent = user_agent
)

top = reddit.subreddit("desabafos").hot(limit = 12)

id = -2
path = "temp"
for submission in top:
    f = open(os.path.join(path, str(id)+".txt"), "w+", encoding="utf-8")
    f.write(submission.title + '\n\n\n' + submission.selftext + '\n\n\n')
    f.close()
    id = id+1