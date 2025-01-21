#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If an HTTPError occurs, it displays the error code.
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send the request
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Handle HTTPError and display the error code
        print("Error code:", e.code)
