#!/usr/bin/python3

"""This module queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'NewAgent'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if (req.status_code == 200):
        for index in range(10):
            print(req.json()['data']['children'][index]['data']['title'])
    else:
        print(None)
