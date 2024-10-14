0x0A. Python - Inheritance
Python-OOP-Inheritance

Inheritance:

Inheritance is a mechanism in object-oriented programming that allows a class (child class) to inherit properties and methods from another class (parent class).
It helps in code reuse and also allows for method overriding, where the child class can modify the behavior of inherited methods.
Multiple Inheritance:

In Python, a class can inherit from more than one parent class. This is called multiple inheritance.
Python uses the Method Resolution Order (MRO) to determine the order in which the parent classes are searched when looking for a method or attribute.
Inheritance in Python:

Python uses classes and objects to implement inheritance.
A child class is created by specifying the parent class(es) in parentheses. For example:
python
Copy code
What is a superclass, base class, or parent class:

A superclass, also known as a base class or parent class, is a class from which other classes (subclasses) inherit attributes and methods. In Python, this is a class that provides common behavior to derived classes. class Parent:
    pass

class Child(Parent):
    pass
Learn to Program 10: Inheritance Magic Methods:

This covers special methods (magic methods) that Python uses for certain operations, like __init__ for initializing an object, or __str__ for returning a string representation of an object.
You may also learn about methods like super() to access the parent class's methods.

subclass:

A subclass is a class that inherits from a parent class (or superclass). It can inherit or override methods and attributes from the parent class. 
 attributes and methods of a class or instance:

You can use the built-in dir() function to list all the attributes and methods of a class or instance.

can an instance have new attributes:

An instance can have new attributes when you assign new variables to it dynamically or through the constructor (__init__ method) or by adding properties manually after the object is created.


