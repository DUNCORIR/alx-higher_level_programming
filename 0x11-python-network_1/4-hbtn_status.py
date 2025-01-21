#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Send a GET request to the URL
    response = requests.get(url)

    # Format the output
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
