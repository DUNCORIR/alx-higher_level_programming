
0x11. Python - Network #1
Description
This project focuses on Python's capabilities for network programming, particularly how to fetch and manipulate data from external services using libraries like urllib and requests. It includes practical tasks to familiarize with HTTP requests, handling JSON responses, and interacting with APIs.

Learning Objectives
By the end of this project, you should be able to explain and demonstrate the following concepts:

General
How to fetch internet resources using the Python package urllib.
How to decode urllib body responses.
How to use the Python package requests (#requestsiswaysimplerthanurllib).
How to make HTTP GET requests.
How to make HTTP POST, PUT, and other requests.
How to fetch JSON resources.
How to manipulate data from an external service.
Resources
Read or Watch:
HOWTO Fetch Internet Resources Using urllib Package
Quickstart with Requests package
Requests package documentation
Requirements
General
Editor: Use vi, vim, or emacs.
Interpreter: Python 3.8.5 on Ubuntu 20.04 LTS.
Code style: Follow pycodestyle (version 2.8.*).
All Python files should be executable and include the shebang #!/usr/bin/python3 as the first line.
Modules, classes, and functions must be documented with meaningful docstrings.
Tasks
0. What's my status? #0
Write a Python script that fetches a URL using urllib and displays its response.

1. Response header value #0
Fetch a URL and display the value of a specific response header using urllib.

2. POST an email #0
Send a POST request to a URL with an email parameter using urllib.

3. Error code #0
Handle HTTP errors while fetching a URL using urllib.

4. What's my status? #1
Fetch a URL using the requests library and display its status.

5. Response header value #1
Fetch a URL and display a specific response header using the requests library.

6. POST an email #1
Send a POST request to a URL with an email parameter using the requests library.

7. Error code #1
Handle HTTP errors while fetching a URL using the requests library.

8. Search API
Interact with a public API, sending search queries, and displaying the results.

9. My Github!
Authenticate with GitHub's API to retrieve user-specific information.

10. Time for an interview!
A technical preparation task focusing on using APIs and JSON data.

Usage
To execute a script:

bash
chmod +x <script_name>.py
./<script_name>.py
For Python scripts that require arguments:

bash
./<script_name>.py <argument>
Author
Duncan Korir