#!/usr/bin/python3
"""Module for task 2 advanced """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    recursive function that queries the Reddit API
    and returns a list containing the titles
    """
    global after
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    responses = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if responses.status_code == 200:
        after_data = responses.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = responses.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
