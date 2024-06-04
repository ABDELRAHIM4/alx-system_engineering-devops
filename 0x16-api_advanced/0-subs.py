#!/usr/bin/python3
"""Write a function that queries the Reddit API"""
import requests
def number_of_subscribers(subreddit):
    """Write a function that queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User_Agent" : "MyUserAgent/1.0"}
    res = requests.get(url, headers= headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data["data"]["subscribers"]
    else:
        return 0
