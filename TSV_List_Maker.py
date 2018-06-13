import praw

# open Reddit instance
reddit = praw.Reddit(client_id='Your client_id',
                     client_secret='Your client_secret',
                     user_agent='Your user_agent')

# open /r/SVExchange instance
subreddit = reddit.subreddit('SVExchange')

# open/create file to append TSVs onto
f = open("tsvfile.txt", "a+")

# cycle through submission instances
for submission in subreddit.new(limit=25): 
    if len(submission.title) == 4:
        f.write(str(submission.title) + "\r\n")
    
f.close()
