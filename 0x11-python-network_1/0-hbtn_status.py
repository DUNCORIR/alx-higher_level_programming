#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
using the urllib package and displays the body of the response.
"#!/usr/bin/python3
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

# Fetch the URL using urllib
with urllib.request.urlopen(url) as response:
    body = response.read()

# Display the required output
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode("utf-8")))
