import configparser

from tweepy import OAuthHandler, API

config = configparser.ConfigParser()
config.read('../config.ini')

consumer_key = config['twitter']['consumer_key']
consumer_key_secret = config['twitter']['consumer_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


def is_verified(tweet_id: str) -> bool:
    '''
    Check whether poster is valid user.
    :param tweet_id:
    :type tweet_id:
    :return:
    :rtype:
    '''
    response = None
    try:
        tweet = api.get_status(tweet_id)
        response = tweet._json['user']['verified']
        return response
    except:
        print(response)
        return response
