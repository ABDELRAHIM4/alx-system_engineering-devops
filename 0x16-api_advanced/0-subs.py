#!/usr/bin/python3
"""Write a function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Write a function that queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/".format(subreddit)
    headers = {"User-Agent": "user-agent"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get("data")
        return (data.get("subscribers"))
    else:
        return (0)
