#!/usr/bin/python3
"""returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[]):
    """returns a list containing the titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "useragent"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return (None)
    results = res.json()
    for j in results.get("children"):
        hot_list.append(c.get("data").get("title"))
    if after in results["data"] and results["data"]["after"]:
        return recurse(subreddit, hot_list)
    return (hot_list)
