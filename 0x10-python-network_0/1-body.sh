#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response only if the status code is 200.
response=$(curl -s -w "%{http_code}" -o response.txt "$1")
if [ "$response" -eq 200 ]; then
  cat response.txt
fi