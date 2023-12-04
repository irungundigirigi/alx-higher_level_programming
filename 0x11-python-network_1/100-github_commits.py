#!/usr/bin/python3
import sys
import requests

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    res = requests.get(url)
    commits = res.json()[:10]

    try:
        for commit in commits:
            print("{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")))
    except IndexError:
        pass    
