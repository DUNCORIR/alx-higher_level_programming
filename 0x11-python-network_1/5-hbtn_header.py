#!/usr/bin/python3
"""
Fetches the X-Request-Id value from the response header.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]  # The URL passed as an argument

    # Send a GET request to the URL
    response = requests.get(url)

    # Retrieve and display the X-Request-Id from the headers
    print(response.headers.get('X-Request-Id'))
