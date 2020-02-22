import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #old account
    client_id = ''
    client_secret = ''
    username = ''
    password = ''

    #new account
    client_id2 = ''
    client_secret2 = ''
    username2 = ''
    password2 = ''

    #user agent required for PRAW to work
    user_agent = 'Reddit account migration bot (by /u/PunyDev)'