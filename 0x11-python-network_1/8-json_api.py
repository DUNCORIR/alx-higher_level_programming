#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with letter
parameter.Handles responses based on the JSON
structure or error codes.
"""
import sys
import requests

if __name__ == "__main__":
    # Get the query letter or set it to an empty string if no argument is given
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send POST request with the parameter 'q'
    try:
        response = requests.post(
            "http://0.0.0.0:5000/search_user", data={'q': q}
        )
        # Try to parse the response as JSON
        try:
            data = response.json()
            if not data:
                print("No result")
            else:
                print(f"[{data.get('id')}] {data.get('name')}")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException:
        print("Request failed")
