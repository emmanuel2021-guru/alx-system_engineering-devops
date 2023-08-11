#!/usr/bin/python3

"""This module queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'New'}
    req = requests.get(url, headers=header,
                       allow_redirects=False, params=after)
    if req.status_code == 200:
        for each in req.json().get('data').get('children'):
            hot_list.append(each['data']['title'])
    new_after = req.json().get('data', {}).get('after')
    if new_after:
        return recurse(subreddit, hot_list=hot_list, after=new_after)
    else:
        return hot_list if hot_list else None
