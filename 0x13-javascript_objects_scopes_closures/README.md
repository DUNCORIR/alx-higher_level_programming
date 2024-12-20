0x13. JavaScript - Objects, Scopes and Closures

Description

This project is focused on understanding JavaScript objects, scopes, and closures. By the end of this project, you will have a solid grasp of creating and working with objects, handling variable scope, leveraging closures, and understanding prototypes and inheritance in JavaScript.

Learning Objectives

By the end of this project, you should be able to:

Explain why JavaScript programming is amazing.

Create objects in JavaScript.

Understand the this keyword and its context.

Explain the concept of undefined in JavaScript.

Recognize the importance of variable types and scopes.

Define and use closures effectively.

Understand what prototypes are and their significance.

Inherit an object from another in JavaScript.

Resources

Read or Watch:

JavaScript object basics

Object-oriented JavaScript (read all examples)

Class - ES6

super - ES6

extends - ES6

Object prototypes

Inheritance in JavaScript

Closures

this/self

Modern JS

Project Tasks

Requirements

General

Allowed editors: vi, vim, emacs

All your files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/node

A README.md file, at the root of the folder of the project, is mandatory

Your code should be semistandard compliant. This includes rules of Standard + semicolons on top (reference: AirBnB style guide)

All your files must be executable

The length of your files will be tested using wc

You are not allowed to use var

Mandatory Tasks:

First Class Objects:
Write a function that returns a new object with specified properties.

Object Methods:
Create a function that demonstrates the use of methods in objects.

Scope and Closures:
Write a function that utilizes closures to maintain state between calls.

Prototypes:
Demonstrate how to add methods to a prototype.

Inheritance:
Create a parent object and inherit from it using Object.create or class syntax.

Advanced Tasks:

Deep Copy:
Create a function to deep-copy an object.

Custom Prototypes:
Extend built-in prototypes for a unique use case (e.g., String or Array).

Using Closures for Encapsulation:
Write a module pattern using closures to encapsulate private variables.

Example Code Snippets

Creating Objects:

const car = {
  brand: "Toyota",
  model: "Corolla",
  year: 2020,
  start: function() {
    console.log("Car started!");
  }
};
car.start(); // Output: Car started!

Using Closures:

function makeCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}
const counter = makeCounter();
console.log(counter()); // Output: 1
console.log(counter()); // Output: 2

Prototypes and Inheritance:

class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}
class Dog extends Animal {
  speak() {
    console.log(`${this.name} barks.`);
  }
}
const dog = new Dog("Rex");
dog.speak(); // Output: Rex barks.

Author

Duncan

For any inquiries or feedback, feel free to contact me at duncorir@gmail.com.