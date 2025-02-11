# 0x14. JavaScript - Web Scraping

## Introduction
Web scraping is a technique used to extract data from websites. In this project, we use JavaScript and Node.js to fetch data from APIs, manipulate JSON data, and read/write files using the `fs` module. This project will introduce you to different ways of making HTTP requests, including the `fetch` API, `request` module (deprecated), and `axios`.

## Learning Objectives
By the end of this project, you should be able to:
- Understand the importance of JavaScript for web scraping.
- Manipulate JSON data effectively.
- Make HTTP requests using `fetch` and `axios`.
- Read and write files using the `fs` module.
- Extract data from HTML using `cheerio`.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on **Ubuntu 20.04 LTS** using **Node.js 14.x**
- All files must end with a new line
- The first line of all files must be `#!/usr/bin/node`
- A `README.md` file at the root of the project directory is mandatory
- Code should follow the **semistandard** style (Standard + semicolons, AirBnB reference)
- Files must be executable
- `var` is not allowed (use `const` or `let` instead)

## Installation
Ensure you have Node.js installed. If not, install it using:

```bash
sudo apt update && sudo apt install -y nodejs npm
```

Verify the installation:

```bash
node -v
npm -v
```

Next, install the necessary dependencies:

```bash
npm install axios cheerio fs
```

## Usage
### Making HTTP Requests
#### Using `fetch`
```js
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

#### Using `axios`
```js
const axios = require('axios');
axios.get('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => console.log(response.data))
  .catch(error => console.error('Error:', error));
```

### Reading and Writing Files with `fs`
#### Reading a File
```js
const fs = require('fs');
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
```

#### Writing to a File
```js
fs.writeFile('output.txt', 'Hello, World!', 'utf8', err => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File written successfully');
});
```

### Web Scraping with `cheerio`
#### Installation
```bash
npm install cheerio axios
```

#### Example Script
```js
const axios = require('axios');
const cheerio = require('cheerio');

axios.get('https://example.com')
  .then(response => {
    const $ = cheerio.load(response.data);
    console.log($('h1').text());
  })
  .catch(error => console.error('Error:', error));
```

## Additional Resources
- [MDN Web Docs - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Axios Documentation](https://axios-http.com/docs/intro)
- [Node.js File System Module](https://nodejs.org/api/fs.html)
- [Cheerio Documentation](https://cheerio.js.org/)

## Author
Duncan Korir - ALX Software Engineering Program


