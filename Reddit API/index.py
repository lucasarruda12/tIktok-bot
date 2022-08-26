import praw

reddit = praw.Reddit(
    client_id = "6UJQEOK_UhVkuhxrzdykVg", 
    client_secret = "49yxZCobgHWaD7W9UuZveZSCrSRS6Q", 
    username ="", 
    password = "", 
    user_agent = "teste"
)

top = reddit.subreddit("memes").top(limit = 5)

for submission in top:
    print(submission.content)