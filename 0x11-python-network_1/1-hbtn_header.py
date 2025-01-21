#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Extract the headers
        headers = response.headers

        # Get the X-Request-Id header value
        x_request_id = headers.get("X-Request-Id")

        # Print the header value
        print(x_request_id)
