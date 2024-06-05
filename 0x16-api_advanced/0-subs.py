#!/usr/bin/python3
"""
Query subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers on a given subreddit"""
    user_agent='MY API_V1'
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json',
    'Origin': 'https://your-website.com',
    'Access-Control-Request-Method': 'GET',
    'Access-Control-Request-Headers': 'Content-Type',
}
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
    print(response)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
