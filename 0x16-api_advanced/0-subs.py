#!/usr/bin/python3
import requests
def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user_agent" : "alx-system_engineering-devops/0x16-api_advanced"}
    res = requests.get(url, headers= headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data["data"]["subscribers"]
    else:
        return 0
