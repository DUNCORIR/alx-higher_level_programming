#!/bin/bash
# The script takes a URL as input then displays the size of the body size in bytes.
curl -s "$1" | wc -c