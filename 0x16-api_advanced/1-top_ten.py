#!/usr/bin/python3
"""Write a function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot"
    headers = {"User-Agent": "userAgent"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
