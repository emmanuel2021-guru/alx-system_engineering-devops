#!/usr/bin/python3

"""This module contains a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of
    subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'NewAgent'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if (req.status_code == 200):
        return req.json()['data']['subscribers']
    else:
        return 0
