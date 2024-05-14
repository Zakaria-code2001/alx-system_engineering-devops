#!/usr/bin/python3
"""Module for task 3 advanced """
import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles
    """

    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {}).get('children', [])

    if not data:
        return None

    for post in data:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            if word.lower() in title:
                word_count[word.lower()] += 1

    after = response.json().get('data', {}).get('after')
    if after:
        count_words(subreddit, word_list, word_count, after)
    else:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
