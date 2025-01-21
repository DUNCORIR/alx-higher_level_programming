#!/usr/bin/python3
"""
This script lists 10  commits (from most recent to oldest)
of repository.
"""

import requests
import sys

if __name__ == "__main__":
    # Get repository and user details

    repository = sys.argv[1]
    owner = sys.argv[2]

    # GitHub API URL for commits of the repository
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        commits = response.json()

        # Print 10 commits
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print("Error: unable to fetch commits.")
