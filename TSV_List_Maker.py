import praw

reddit = praw.Reddit(client_id='your client_id',
                     client_secret='your client_secret',
                     user_agent='your user_agent')

subreddit = reddit.subreddit('SVExchange')

with open("tsvfile.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

f = open("tsvfile.txt", "a")

for submission in subreddit.new(limit=50):
    if len(submission.title) == 4:
        if (str(submission.title) + "\r\n") not in array:
            f.write(str(submission.title) + "\r\n")

f.close()
