import praw
import json
import pprint
from sys import argv

user_password = argv[1]


reddit = praw.Reddit(client_id = '',
        client_secret = '',
        password = user_password,
        user_agent = 'asdf',
        username = '')

karma = reddit.get('/api/v1/me/karma')
with open('karmaJSON.txt', 'w') as outfile:
        json.dump(karma, outfile)
pprint.pprint(karma)
