#!/usr/bin/python3
"""
Uses the GitHub API with Basic Authentication to fetch the user ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Get GitHub username & personal access-token from command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(
        "https://api.github.com/user", auth=HTTPBasicAuth(username, token)
    )

    # If the request was successful, display the user ID
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        print("Authentication failed or invalid data")
