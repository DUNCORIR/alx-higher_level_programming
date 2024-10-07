0x08. Python - More Classes and Objects

Python
OOP (Object-Oriented Programming)
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects rather than functions and logic. Objects are instances of classes, which can contain data (attributes) and code (methods).

Key Concepts of OOP:
Classes and Objects:

Class: A blueprint for creating objects. Defines a set of attributes and methods.
Object: An instance of a class. Represents a specific entity with its own state.
Encapsulation:

Bundling data and methods that operate on the data within one unit (class).
Restricts direct access to some of an object's components, which is a means of preventing accidental interference and misuse.
Inheritance:

Mechanism where a new class (child/subclass) inherits attributes and methods from an existing class (parent/superclass).
Promotes code reusability and establishes a natural hierarchy.
Polymorphism:

Ability to present the same interface for different underlying forms (data types).
Allows methods to do different things based on the object it is acting upon.
Abstraction:

Hiding complex implementation details and showing only the necessary features of an object.
Simplifies interaction with objects by exposing only relevant parts.

What is a Class
A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) will have.

Key Components of a Class:
Attributes: Variables that hold data specific to the class or instances.
Methods: Functions defined within a class that describe the behaviors of the objects.
Docstrings: Documentation strings that describe the purpose of the class and its components.

What is an Object and an Instance.
Object: An entity that has state and behavior. In OOP, objects are instances of classes.

Instance: A specific object created from a class. Each instance can have unique attribute values.

Difference Between a Class and an Object or Instance
Class:

Blueprint or template.
Defines a set of attributes and methods.
Not tied to any specific data.
Object/Instance:

Concrete entity created from a class.
Holds specific data.
Can interact with other objects.

What is an Attribute
An attribute is a variable that holds data associated with a class or its instances.

Types of Attributes:
Class Attributes:

Shared across all instances of the class.
Defined directly within the class, outside any methods.

Instance Attributes:

Unique to each instance.
Defined within methods (usually __init__).

Public, Protected, and Private Attributes
Python uses a naming convention to indicate the intended access level of attributes:

Public Attributes:

Accessible from anywhere.
No leading underscores.
Protected Attributes:

Intended to be accessed within the class and its subclasses.
Single leading underscore (_).
Private Attributes:

Intended to be accessed only within the class.
Double leading underscores (__), which trigger name mangling.


Name Mangling for Private Attributes:
Private attributes are internally renamed to include the class name to prevent accidental access

What is self
self refers to the instance of the class. It is used to access attributes and methods within the class.

Key Points:
First Parameter: self is always the first parameter in instance methods.
Represents the Instance: Allows access to the instance's attributes and methods.
Not a Keyword: self is a naming convention, but you can technically name it differently (though not recommended).

What is a Method
A method is a function defined within a class that operates on instances of that class.

Types of Methods:
Instance Methods:

Operate on instances of the class.
Access and modify instance attributes.

Class Methods:

Operate on the class itself, not on instances.
Use the @classmethod decorator.
Take cls as the first parameter.

Static Methods:

Do not operate on class or instance.
Use the @staticmethod decorator.
Behave like regular functions but belong to the class's namespace.

The Special __init__ Method and How to Use It
The __init__ method in Python is a special method called a constructor. It initializes a newly created object.

Key Points:
Automatic Invocation: Called automatically when a new instance is created.
Initializes Attributes: Sets up initial state by assigning values to instance attributes.
No Return Value: Should return None.


