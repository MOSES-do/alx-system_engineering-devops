#!/usr/bin/python3
"""
Query subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "learn_api by ACE_MOSES"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        print(response.status_code)
        print(response.json)
        return 0
