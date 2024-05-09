#!/usr/bin/python3
"""Module for task 2 advanced """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API
    and returns a list containing the titles.
    """
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    responses = requests.get(url, params=params,
                             headers=user_agent, allow_redirects=False)

    if responses.status_code == 200:
        data = responses.json().get("data")
        after_data = data.get("after")
        if after_data is not None:
            # Update the 'after' parameter for the next recursive call
            after = after_data
            # Make the recursive call with the updated 'after' parameter
            recurse(subreddit, hot_list, after)
        all_titles = data.get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None
