import tweepy
import csv

API_KEY = 'JJdmppbq0mo9zDgMQ5dpgGoDI'
API_SECRET = 'KIz0BaXjGbAKl5aUBMYbKOTsltWcOdUsyRhtL3uujIDeWFunV4'
BEARER_TOKEN = (
    'AAAAAAAAAAAAAAAAAAAAADEkaAEAAAAASR652IkwAl%2FZTDTLecq4zcyjdbg%3DJKXP3FI9IvcF8dOq5FVmKD1NmTAJt7d0gfVVlDKGSKGoW625a7'
)
ACCESS_TOKEN = '1501486871158804481-eK5c3oZt2aI09GXNY9XDcyvXq7D8jW'
ACCESS_TOKEN_SECRET = 'ouSeRorHC6cmuyHpRKDxUJ8lyd7hb8acrDOC1jTYE7wLU'
company = 'GitHubHelp'

def get_all_tweets(screen_name):

    # authorize twitter, initialize tweepy tweets
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    user = api.get_user(screen_name=screen_name)

    tweets = client.get_users_mentions(
        id=user.id,
        tweet_fields=['created_at', 'conversation_id', 'public_metrics'],
        expansions=['author_id'],
        max_results=100,
    )

    outtweets = [
        [
            company,
            'https://twitter.com/i/user/{}'.format(tweet.author_id),
            'https://twitter.com/twitter/statuses/{}'.format(tweet.id),
            tweet.text,
            str(tweet.created_at.date()),
            str(tweet.public_metrics['retweet_count']),
            str(tweet.public_metrics['like_count']),
        ]
        for tweet in tweets.data
    ]

    with open('{}_tweets.csv'.format(screen_name), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Company", "Twitter Handle", "Tweet Link", "Tweet text", "Date", "Num Retweets", "Num Likes"])
        writer.writerows(outtweets)
        print('{}_tweets.csv was successfully created.'.format(screen_name))
    pass


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets(company)
