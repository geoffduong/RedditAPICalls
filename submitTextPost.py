import praw
from sys import argv

user_password = argv[1]

reddit = praw.Reddit(client_id = '',
        client_secret = '',
        password = user_password,
        user_agent = 'asdf',
        username = '')

reddit.subreddit('test').submit(title = 'test',
        selftext = 'testtesttesttesttesttesttest')
