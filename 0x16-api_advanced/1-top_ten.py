#!/usr/bin/python3
"""
This fucntion will query the REddit API and print the titles of 
the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    if not a valid subreddi, print None.
    """
    reqs = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )
    if reqs.status_code == 200:
        for get_data in reqs.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)