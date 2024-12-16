0x12. JavaScript - Warm up

Welcome to the 0x12. JavaScript - Warm up project! This README file provides an overview of the project, including instructions for running the scripts, coding style requirements, and details on the key topics covered.

Table of Contents

Introduction

Project Environment

Requirements

Getting Started

Key Topics Covered

Project Structure

Usage

References

Introduction

This project is part of the curriculum for learning JavaScript programming. It introduces essential JavaScript concepts and syntax to build a solid foundation for further projects. You will explore variables, data types, functions, loops, and more while adhering to best practices in coding.

Project Environment

The scripts in this project are executed on Ubuntu 20.04 LTS using Node.js version 14.x. It is essential to develop and test your code in this environment to ensure compatibility.

Requirements

All files must:

Start with the line: #!/usr/bin/node

Be executable using chmod +x

End with a new line

Coding style must adhere to Semistandard:

Based on Standard JS

Requires semicolons (;) at the end of statements

Compatible with Airbnb Style Guide

A README.md file at the root of the project folder is mandatory.

Semistandard Installation

To install and use Semistandard:

npm install semistandard --global

Check your code compliance:

semistandard <filename>.js

Getting Started

Setup

Install Node.js (version 14.x) on your system.

Clone the repository containing this project:

git clone <repository_url>

Navigate to the project folder:

cd 0x12-javascript-warm_up

Make Files Executable

Run the following command for each script to make it executable:

chmod +x <filename>.js

Run the Scripts

To execute a script, use:

./<filename>.js

Key Topics Covered

1. Writing JavaScript Code

Basics of JavaScript syntax

Adding comments and structuring code

2. Variables

Understanding var, let, and const

Differences in scope and usage

3. Data Types

Primitive types: string, number, boolean, undefined, null, symbol, bigint

Object types: Arrays, dictionaries (objects)

4. Operators and Operator Precedence

Arithmetic, logical, comparison, and assignment operators

Understanding operator precedence for complex expressions

5. Controlling Program Flow

if, if...else, and switch statements

Loops: for, while, and do...while

Using break and continue

6. Functions

Defining and using functions

Function parameters and return values

Arrow functions and their scope behavior

7. Objects and Arrays

Creating and manipulating objects and arrays

Accessing and modifying properties and elements

8. Intrinsic Objects

Understanding built-in objects like Math, Date, and RegExp

9. Module Patterns

Importing and exporting modules

Using ES6 module syntax (import and export)

10. Modern JavaScript (ES6)

Template literals

Destructuring

Spread/rest operators

Default parameters

Promises and async/await

Project Structure

Below is an example structure of the project:

0x12-javascript-warm_up/
├── 0-javascript_is_amazing.js
├── 1-variable.js
├── 2-data_types.js
├── 3-operator_precedence.js
├── 4-control_flow.js
├── 5-functions.js
├── 6-objects_arrays.js
├── 7-modern_js_features.js
├── README.md

Usage

To execute a script, follow these steps:

Make sure the script is executable:

chmod +x <filename>.js

Run the script:

./<filename>.js

Example

For the file 0-javascript_is_amazing.js:

chmod +x 0-javascript_is_amazing.js
./0-javascript_is_amazing.js

References

JavaScript on MDN Web Docs

Node.js Documentation

Semistandard Documentation

Airbnb JavaScript Style Guide
