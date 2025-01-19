#!/bin/bash
# Sends a POST request with contents of a JSON file to the specified URL
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
