#!/usr/bin/python3
"""Write a function that queries the Reddit API"""
import requests
def number_of_subscribers(subreddit):
    """Write a function that queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user_agent" : "alx-system_engineering-devops/0x16-api_advanced"}
    res = requests.get(url, headers= headers, allow_redirects=False)
    print(res.status_code)
    if res.status_code == 200:
        data = res.json()
        print(data)
        return data["data"]["subscribers"]
    else:
        return 0
