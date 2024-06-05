#!/usr/bin/python3
import praw
"""
Query subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers on a given subreddit"""
    user_agent='MY API_V1'
    reddit = praw.Reddit(
                        client_id='qp3ut-6a7Yfzaz1gNdNfKQ',
                        client_secret='9G1mQTBbXaMk85c2nhagiom_3s2XLQ',
                        user_agent='MY API_V1'
                    )
    subreddit = reddit.subreddit(subreddit)
    return subreddit.subscribers
