#!/usr/bin/python3
"""
Script sends a POST request to URL with email parameter
and displays the body of the response
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create the POST request
    request = urllib.request.Request(url, data=data)

    # Send request and get the response
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8S'))
