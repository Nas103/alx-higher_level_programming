#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest)
of a specified repository by the specified owner using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
