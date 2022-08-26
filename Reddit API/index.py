import praw

reddit = praw.Reddit(
    client_id = "", 
    client_secret = "", 
    username ="", 
    password = "", 
    user_agent = "teste"
)

top = reddit.subreddit("memes").top(limit = 5)

for submission in top:
    print(submission.content)