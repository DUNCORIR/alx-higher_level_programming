#!/bin/bash
# The script takes a URL as input then displays the size of the body of the response in bytes.
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'