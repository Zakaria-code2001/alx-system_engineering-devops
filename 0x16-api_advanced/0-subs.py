#!/usr/bin/python3
"""Module for task 0 advanced API"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers.
    If the subreddit is not valid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    else:
        return 0