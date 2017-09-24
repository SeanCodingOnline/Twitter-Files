import vulners, random, time, datetime
import tweepy

#Twitter OAuth - From Twitter 'apps'
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Call Tweepy api instance
api = tweepy.API(auth, wait_on_rate_limit='true')

vulners_api = vulners.Vulners()
vulns = vulners_api.search("")

today_date = datetime.date.today()
api.update_status('TEXT IN YOUR MAIN POST TO REPLY TO' + today_date + 'MORE TEXT')

#reply to main post with replies created and found in file1
count = 1
with open('vulners.txt', 'w') as file1:
    for line in vulns:
        title = str(line.get('title'))
        file1.write("(" + str(count)+ ")" + "CVSS:" + str(line.get('cvss')['score']) + " " + title[:85] + " " + str(line.get('href')) + "\n")
        count = count+1

user = 'your_twitter_@handle'
for status in tweepy.Cursor(api.user_timeline, id=user).items(1):
    with open('vulners.txt','r') as file1:
        for line in file1:
            sleep_timer = (random.randint(60,80))
            api.update_status('@yourname' + line, status.id)
            print('Tweeting: ' + line)
            time.sleep(sleep_timer)
