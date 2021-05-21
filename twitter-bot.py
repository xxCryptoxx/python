import tweepy
# NOTE TWITTER ALLOWS 2,400 TWEETS PER DAY...sadly :/
# Get keys from https://developer.twitter.com/en

def secret():
    consumer_key = 'API_KEY_HERE'
    consumer_secret = 'API_SECRET_KEY_HERE'
    access_token = 'ACCESS_TOKEN_HERE'
    access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'
    
    authorize(consumer_key, consumer_secret, access_token, access_token_secret)

def authorize(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    main(auth)

def main(auth):
    api = tweepy.API(auth)
    user = api.me()

    print('I am ' + user.name)

    #user_id=  elonmusk----geekulcha----spacex------tesla
    user_id = '44196397', '728018491', '34743251', '13298072'
    lang='en'
    numberOfTweets = 200 # Amount of tweets you want retweeted

    for theid in user_id:
        for tweet in tweepy.Cursor(api.user_timeline, id=theid, lang="en").items(numberOfTweets):
            try:
                print('Tweet from: @' + tweet.user.screen_name)
                tweet.favorite() # Like
                tweet.retweet() # Retweet
                print('You Just Retweeted A Tweet :)')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

if __name__ == "__main__":
    secret()
