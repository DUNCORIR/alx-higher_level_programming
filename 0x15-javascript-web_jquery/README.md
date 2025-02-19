# 0x15. JavaScript - Web jQuery

## **Project Overview**
This project introduces **jQuery**, a fast and lightweight JavaScript library that simplifies **HTML document traversal, event handling, animation, and AJAX interactions**. By leveraging jQuery, front-end development becomes more efficient, making websites more interactive and user-friendly.

## **Learning Objectives**
By the end of this project, you will be able to:
- Explain why jQuery makes front-end programming easier.
- Select HTML elements using JavaScript and jQuery.
- Differentiate between ID, class, and tag name selectors.
- Modify an HTML element’s **style**, **content**, and **structure**.
- Handle **DOM events** and listen to **user interactions**.
- Perform **GET** and **POST** requests using jQuery AJAX.
- Debug JavaScript and handle errors effectively.

## **Resources**
To grasp the concepts in this project, review the following:
- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [Selectors in jQuery](https://api.jquery.com/category/selectors/)
- [Modifying HTML & CSS with jQuery](https://www.w3schools.com/jquery/jquery_dom_get.asp)
- [AJAX Requests with jQuery](https://www.w3schools.com/jquery/jquery_ajax_intro.asp)
- [Handling JavaScript Errors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)

## **Project Requirements**
### **General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files must be **executable**.
- All files should end with a **new line**.
- Your code should be properly **documented**.
- HTML files should not be **minified**.
- Follow the **semistandard** style guide:
  - [JavaScript Standard Style](https://standardjs.com/)
  - Includes **semicolons** (`;` required).
- Your JavaScript code should run in the browser.

### **Environment**
- OS: **Ubuntu 20.04 LTS**
- Browser: **Google Chrome (latest stable)**
- jQuery Version: **jQuery 3.x** (loaded via CDN)
- Language: **JavaScript (ECMAScript 6)**

## **Installation**
To use jQuery in your HTML files, include the jQuery CDN before your JavaScript scripts:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My jQuery Project</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Hello, jQuery!</h1>
</body>
</html>
```

## **Core Concepts**
### **1. Selecting Elements in jQuery**
```js
// Select by ID
$("#myId").css("color", "blue");

// Select by class
$(".myClass").hide();

// Select all paragraphs
$("p").text("Updated paragraph content");
```

### **2. Modifying Content and Styles**
```js
$("#title").text("New Title");  // Change text
$("#box").css("background-color", "red"); // Change style
```

### **3. Handling Events**
```js
$("#button").click(function() {
    alert("Button Clicked!");
});
```

### **4. Modifying the DOM**
```js
// Add a new element
$("#container").append("<p>New Paragraph!</p>");

// Remove an element
$(".oldElement").remove();
```

### **5. AJAX Requests**
```js
// GET request
$.get("https://jsonplaceholder.typicode.com/posts/1", function(data) {
    console.log(data);
});

// POST request
$.post("https://jsonplaceholder.typicode.com/posts", {title: "Hello"}, function(response) {
    console.log(response);
});
```

## **Project Tasks**
| Task # | Task Description |
|--------|-----------------|
| 0 | Select elements using jQuery |
| 1 | Modify element content and styles |
| 2 | Handle user events (clicks, keypress, etc.) |
| 3 | Dynamically modify the DOM (add/remove elements) |
| 4 | Perform AJAX requests with GET and POST |

## **Author**
- Duncan Korir
- GitHub: Duncorir
- Email: duncorir@gmail.com