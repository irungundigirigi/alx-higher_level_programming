#!/usr/bin/python3
import sys
import requests

if __name__ == '__main__':
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    res = requests.get(url)
    commits = res.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass    
