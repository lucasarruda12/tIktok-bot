import praw
from credentials import *
import pyttsx3
from playwright.sync_api import sync_playwright
import os
from createVideo import createClip

# GET REDDIT SUBMISSION
print('[REDDIT] Getting submissions...')
reddit = praw.Reddit(
    client_id = client_id, 
    client_secret = client_secret, 
    username = username, 
    password =  password, 
    user_agent = user_agent
)

top = reddit.subreddit("desabafos").hot(limit = 3)

# SET UP TEXT-TO-SPEAK
print('[TEXT-TO-SPEAK] Setting up text-to-speak...')
engine = pyttsx3.init()

rate = engine.getProperty('rate')                
engine.setProperty('rate', 275) 

# SET UP POST SCREENSHOT
def capture(url: str, id:int) -> None:
    print('[SCREENSHOT] Getting full page...')
    page = p.chromium.launch().new_page()
    page.set_viewport_size({"width": 720, "height": 660})
    page.goto(url)

    print('[SCREENSHOT] Taking screenshot...')
    try:
        posts = page.locator("data-testid=post-container")
        posts.first.screenshot(path=os.path.join('temp', str(id)+".jpg"))
    except:
        print('[SCREENSHOT] Erro de comunicação com o sistema.')
    

# TEXT-TO-SPEAK FUNCTION -> SAVE TO FILE
id= -2
for submission in top:
    texto = str(submission.title + submission.selftext)
    if(len(texto) < 1115):

        print('[TEXT-TO-SPEAK] Creating audio file ['+ submission.title+']...')
        engine.save_to_file(texto, os.path.join('temp', str(id)+".mp3"))
        engine.runAndWait()

        print('[SCREENSHOT] Starting playwright...')
        with sync_playwright() as p:
            capture(submission.url, id)
            p.chromium.launch().close()

            createClip(id)
            id = id+1
