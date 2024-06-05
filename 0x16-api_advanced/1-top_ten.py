#!/usr/bin/python3
'''
    top_ten module
'''
import requests


def top_ten(subreddit):
    '''returns the top ten posts for a given subreddit'''
    user = {'User-Agent': 'MY API_V1'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit)).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)
