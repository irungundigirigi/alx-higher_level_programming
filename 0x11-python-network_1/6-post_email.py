#!/usr/bin/python3
"""Sends a POST request  with a given email as body.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    r = requests.post(url, data=email)
    print(r.text)
