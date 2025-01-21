#!/usr/bin/python3
"""
Sends a GET request to a URL and displays the response body.
Handles errors with status codes >= 400.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]  # URL passed as the first argument

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the status code is >= 400
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
