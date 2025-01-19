#!/bin/bash
# Makes request to 0.0.0.0:5000/catch_me and causes server to respond with "You got me!"
curl -s -X PUT 0.0.0.0:5000/catch_me
