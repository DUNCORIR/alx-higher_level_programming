# 0x10. Python - Network #0

## Project Overview

This project involves understanding the fundamentals of HTTP, including making HTTP requests, interpreting URLs, managing HTTP headers and cookies, and handling HTTP responses. You will learn to explain key concepts related to HTTP and network communication in the context of the web. The project involves using `curl` to interact with web servers and understanding how HTTP methods and status codes work.

## Learning Objectives

By the end of this project, you will be able to explain the following concepts clearly and confidently:

### General Concepts

- **What a URL is**: A URL (Uniform Resource Locator) is a reference or address used to access resources on the web. It consists of several parts including the protocol (scheme), domain name, and path.
  
- **What HTTP is**: HTTP (Hypertext Transfer Protocol) is the foundation of any data exchange on the Web. It is a protocol used for transmitting hypertext via the internet.

- **How to Read a URL**: Understanding the structure of a URL, including how to distinguish between the scheme, domain name, port, path, query string, and fragment.

- **The Scheme for an HTTP URL**: The scheme in a URL indicates the protocol used to access the resource, such as `http`, `https`, `ftp`, etc.

- **What a Domain Name is**: A domain name is the human-readable address used to identify a resource on the internet (e.g., `www.google.com`).

- **What a Sub-domain is**: A sub-domain is a part of a larger domain, which can be used to organize and navigate different sections of a website (e.g., `api.google.com` is a sub-domain of `google.com`).

- **How to Define a Port Number in a URL**: The port number is an optional part of the URL that specifies which network port on the server should handle the request (e.g., `http://example.com:8080`).

- **What a Query String is**: A query string is a part of a URL that contains parameters passed to the server, usually in the form of `key=value` pairs (e.g., `?name=John&age=30`).

### HTTP Request and Response

- **What an HTTP Request is**: An HTTP request is a message sent from a client to a server to request a resource. It consists of a method (e.g., GET, POST), a URL, headers, and an optional body.

- **What an HTTP Response is**: An HTTP response is the server's answer to an HTTP request, including status information, headers, and the requested content (or error messages).

- **What HTTP Headers Are**: HTTP headers are metadata about the HTTP request or response, such as the type of content, the user agent, cookies, etc.

- **What the HTTP Message Body is**: The body of the message typically contains the resource requested or a response to the request, such as HTML, JSON, or an image file.

- **What an HTTP Request Method is**: HTTP request methods specify the action to be performed on the resource (e.g., GET, POST, PUT, DELETE).

- **What an HTTP Response Status Code is**: HTTP status codes indicate the result of the request, such as 200 (OK), 404 (Not Found), 500 (Server Error), etc.

- **What an HTTP Cookie is**: An HTTP cookie is a small piece of data sent from the server to the client and stored in the client’s browser. Cookies are used for session management, tracking, and personalizing web content.

### Making HTTP Requests

- **How to Make a Request with cURL**: `cURL` is a tool used to make HTTP requests from the command line. You can use it to send requests and display responses, such as fetching web pages or interacting with APIs.

- **What Happens When You Type google.com in Your Browser (Application Level)**: When you type a URL like `google.com`, the browser performs several steps:
  1. Resolves the domain to an IP address using DNS.
  2. Establishes a connection to the server using the TCP/IP protocol.
  3. Sends an HTTP request for the requested resource (e.g., `GET /`).
  4. The server responds with the requested resource (HTML, images, etc.).
  5. The browser renders the content for display.

## Resources to Read or Watch:
1. **HTTP (HyperText Transfer Protocol)**: Understand the core concepts and mechanisms of HTTP, including how clients and servers communicate over the web.
   
2. **HTTP Cookies**: Learn how cookies are used to store information on the client-side for state management, tracking, and session handling.

---

## Tasks to Complete:

### 0. **Basic HTTP Request Handling**
   - Learn to send basic requests using tools like `curl` and handle HTTP response codes, headers, and bodies.
   
### 1. **HTTP Methods**
   - Understand the different HTTP request methods, such as GET, POST, PUT, DELETE, and how they affect interactions with a web server.

### 2. **Working with URLs and Query Strings**
   - Learn to read and construct URLs, including how to manage query strings and URL parameters.

### 3. **HTTP Response Status Codes**
   - Understand how different HTTP response status codes work, what they indicate, and how to handle them.

### 4. **Cookies in HTTP Requests**
   - Learn how cookies are handled in HTTP requests and responses.

---

## Deliverables:

- Implement scripts or code snippets that interact with web servers via HTTP requests using `curl`.
- Demonstrate an understanding of URL structure, HTTP request methods, and response status codes by completing the project tasks.

By completing this project, you will gain a solid understanding of how web communication works at the HTTP level and will be prepared to handle common tasks such as making API calls, troubleshooting network issues, and managing web traffic.
