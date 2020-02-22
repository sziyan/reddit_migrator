import praw
from config import Config

#initialize reddit instances (reddit is new account, reddit2 is old account)
reddit = praw.Reddit(client_id=Config.client_id2, client_secret=Config.client_secret2, username=Config.username2, password=Config.password2, user_agent=Config.user_agent)
reddit2 = praw.Reddit(client_id=Config.client_id, client_secret=Config.client_secret, username=Config.username, password=Config.password, user_agent=Config.user_agent)

user2 = reddit2.user
subscribe_fail = []
count = 0

#migrate subreddits to new account

print('Migrating subreddits..')
for s in user2.subreddits(limit=None):
    try:
        count += 1
        new_subreddit = reddit.subreddit(s.display_name)
        new_subreddit.subscribe()
        print('Subscribed to {} successfully.'.format(s.display_name))
    except:
        print('Error subscribing to {}'.format(s.display_name))
        subscribe_fail.append(s.display_name)

#output info
print('Subreddit subscribed successfully: {} \nFailure to join the following subs: \n\n {}'.format(count,'\n'.join(subscribe_fail)))

#migrate multireddit

for s in user2.multireddits():
    try:
        subs = []
        for i in s.subreddits:
            subreddit = reddit.subreddit(i.display_name)
            subs.append(subreddit)
        reddit.multireddit.create(s.display_name, subs)
    except:
        print('Error creating some multireddit')
print('Multireddit created successfully..')