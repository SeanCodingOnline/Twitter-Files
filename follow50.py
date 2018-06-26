import tweepy
import time, random
from keys import keys

#Twitter OAuth - From Twitter 'apps', entire calid auth information in keys.py file and add your own keys.py to .gitignore
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Call Tweepy api instance
api = tweepy.API(auth)

friends = api.friends_ids(api.me().id)
possible_hashtags = ['term1','term2','term3']
hashtag_to_search = random.choice(possible_hashtags)
count = 1
for line in tweepy.Cursor(api.search, q=hashtag_to_search).items():
    if count < 50:
        if line.user.id != api.me().id:
            if line.user.id in friends:
                print("You already follow " + line.user.screen_name + "...")
            else:
                sleep_timer = (random.randint(15, 40))
                try:
                    api.create_friendship(screen_name = line.user.screen_name)
                    print(str(count) + ". " + line.user.screen_name + ' from ' + hashtag_to_search)
                    print("Sleeping for " + str(sleep_timer) + " seconds!")
                    count = count + 1
                    friends.append(line.user.id)
                    time.sleep(sleep_timer)
                except Exception:
                    pass
    if count == 50:
        print("Stopping...")
        quit()
