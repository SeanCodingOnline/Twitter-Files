import tweepy
import time, random

#Twitter OAuth - From Twitter 'apps'
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Call Tweepy api instance
api = tweepy.API(auth, wait_on_rate_limit='true')

bad_word = 'marketing'
count = 1
goodcount = 1
for line in tweepy.Cursor(api.friends).items():
    if count < 200:
        description = line.description
        if not bad_word in description:
            print('All good words!' + '[' + str(goodcount) + ']')
            goodcount = goodcount+1
            time.sleep(1)
        elif bad_word in description:
            sleep_timer = (random.randint(15, 30))
            screen_name = line.screen_name
            api.destroy_friendship(screen_name)
            print(str(count) + ". " + "Removed " + str(screen_name) + " from friends. "
                  + "Sleeping for " + str(sleep_timer) + " seconds.")
            count = count+1
            time.sleep(sleep_timer)
        else:
            pass
    if count == 200:
        print("Stopping...")
        quit()