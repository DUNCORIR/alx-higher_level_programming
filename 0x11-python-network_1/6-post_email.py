#!/usr/bin/python3
"""
Sends a POST request with an email as a parameter
and displays the response body.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]  # URL passed as the first argument
    email = sys.argv[2]  # Email passed as the second argument

    # Send a POST request with email in the data
    response = requests.post(url, data={'email': email})

    # Display the body of the response
    print(response.text)
