#!/usr/bin/python3
import requests

def fetch_hot_titles(subreddit, after=None, titles=[]):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'NewAgent'}
    params = {'limit': 25, 'after': after}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if 'data' in data and 'children' in data['data']:
        titles.extend([post['data']['title'] for post in data['data']['children']])
    
    new_after = data.get('data', {}).get('after')
    
    if new_after:
        return fetch_hot_titles(subreddit, after=new_after, titles=titles)
    else:
        return titles if titles else None

if __name__ == '__main__':
    subreddit_name = 'programming'  # Replace with the desired subreddit
    result = fetch_hot_titles(subreddit_name)
    
    if result is None:
        print("No results found for the given subreddit.")
    else:
        for title in result:
            print(title)
