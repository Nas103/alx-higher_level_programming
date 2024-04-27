#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token
as password to access to your information
(only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case,
a personal access token as password)
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))
    print(response.json().get('id', None))
