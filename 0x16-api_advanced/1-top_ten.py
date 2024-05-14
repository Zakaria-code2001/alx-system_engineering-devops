#!/usr/bin/python3
"""Module for task 1 advanced """
import requests
import sys


def top_ten(subreddit):
    """
    function that queries the Reddit API and
    returns 10 titles
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post.get('data').get('title')
            print(title)
    elif (not response.ok):
        return print(None)
