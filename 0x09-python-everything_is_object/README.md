0x09. Python - Everything is object
Python
OOP

What is an Object
An object in Python is an instance of a data structure that contains data (attributes) and behavior (methods). Everything in Python is an object, including numbers, strings, lists, and functions. Objects are created from classes, which define their structure and behavior.

Difference Between a Class and an Object (or Instance)
Class: A blueprint for creating objects. It defines attributes and methods that the objects created from the class will have.
Object/Instance: A specific realization of a class. When a class is instantiated, an object is created. Each object can have different values for its attributes.
Difference Between Immutable Object and Mutable Object
Immutable Object: An object whose state cannot be modified after it is created. Examples include strings, tuples, and frozensets.
Mutable Object: An object whose state can be modified. Examples include lists, dictionaries, and sets.
What is a Reference
A reference in Python is a name that points to an object in memory. When you assign a variable to an object, you're creating a reference to that object.

What is an Assignment
An assignment in Python is the process of binding a variable name to an object. This allows you to access or manipulate the object using the variable name.

What is an Alias
An alias is another name that refers to the same object in memory. When two or more variables point to the same object, they are considered aliases for that object.

How to Know if Two Variables are Identical
You can check if two variables are identical (i.e., refer to the same object) using the is operator. For example:

python
Copy code
a is b  # Returns True if a and b refer to the same object
How to Know if Two Variables are Linked to the Same Object
You can use the id() function to get the unique identifier (memory address) of an object. If two variables have the same id(), they refer to the same object. Example:

python
Copy code
id(a) == id(b)  # Returns True if a and b point to the same object
How to Display the Variable Identifier
In Python, you can use the id() function to display the memory address (identifier) of a variable:

python
Copy code
print(id(variable))
What is Mutable and Immutable
Mutable: Refers to objects that can change their state or content. Examples include lists and dictionaries.
Immutable: Refers to objects that cannot change their state or content once created. Examples include strings and tuples.
Built-in Mutable Types
Lists
Dictionaries
Sets
Built-in Immutable Types
Integers
Floats
Strings
Tuples
Frozensets
How Does Python Pass Variables to Functions
Python uses a mechanism called "pass-by-object-reference" or "pass-by-assignment". This means that when you pass a variable to a function, you are passing a reference to the object, not the actual object itself. If the object is mutable, changes made to it within the function will affect the original object. However, if the object is immutable, you cannot change it, and any "changes" will result in the creation of a new object.
