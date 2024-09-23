#!/usr/bin/python3
"""
tis function queries the Reddit API and returns the number of Reddit subscribers(nor active users totla subscribers) for a given subreddit.
if an invalid subreddit is given, the function should retur 0
"""

import requests

def number_of_subscribers(subreddit):
    """
    if not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0