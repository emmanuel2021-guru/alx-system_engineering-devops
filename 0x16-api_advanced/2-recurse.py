#!/usr/bin/python3

"""This module queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'NewAgent'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if after is None:
        req = requests.get(url, headers=header, allow_redirects=False)
        if (req.status_code == 200):
            for data in req.json()['data']['children']:
                hot_list.append(data['data']['title'])
        after = req.json()['data']['after']
        recurse(subreddit, hot_list, after)
    else:
        if req.json()['data']['after']:
            param = req.json()['data']['after']
            req = requests.get(url, headers=header, allow_redirects=False, params=after)
            if (req.status_code == 200):
                for data in req.json()['data']['children']:
                    hot_list.append(data['data']['title'])
            recurse(subreddit, hot_list, after)
        else:
            req = requests.get(url, headers=header, allow_redirects=False)
            if (req.status_code == 200):
                for data in req.json()['data']['children']:
                    hot_list.append(data['data']['title'])
