0x06. Python - Classes and Objects


0. class
A class is a blueprint for creating objects. It defines attributes (variables) and methods (functions) that the objects created from the class will have.

1. object and an instance
An object is an entity that contains data and methods. An instance is a concrete occurrence of any object. In simpler terms, an instance is the actual object created from a class.

2. Difference between a class and an object/instance
A class is a blueprint, while an object/instance is a realized version of that blueprint with specific data.

3. What is an attribute
Attributes are variables that belong to a class or an instance. They represent the data stored in an object.

4. Public, protected, and private attributes
Public attributes: Accessible from anywhere (e.g., self.name).
Protected attributes: Meant to be accessed only within the class and its subclasses (conventionally prefixed with a single underscore, e.g., _name).
Private attributes: Intended for internal use only within the class (prefixed with double underscores, e.g., __name).

5. What is self
self represents the instance of the class. It is used to access attributes and methods of the current object.

6. What is a method
A method is a function defined within a class. It operates on the data contained in an instance.

7. What is the special __init__ method and how to use it
__init__ is a constructor method that initializes an object's attributes when it's created. It runs automatically when you create an instance of a class.

8. What is Data Abstraction, Data Encapsulation, and Information Hiding
Data Abstraction: Hiding complex details and showing only the necessary parts of the object.
Data Encapsulation: Bundling data (attributes) and methods that operate on the data within one unit (class).
Information Hiding: Restricting access to certain details of an object (e.g., using private attributes).

9. What is a property
A property is a way to control access to instance attributes, allowing you to use getters and setters in a Pythonic way without directly accessing attributes.

10. Difference between an attribute and a property in Python
An attribute is a direct variable in an object. A property uses getter/setter methods to access or modify an attribute, offering more control.

11.  Pythonic way to write getters and setters
Use the @property decorator for getters and @<property_name>.setter for setters instead of defining get_ and set_ methods.

12. How to dynamically create arbitrary new attributes for existing instances of a class
You can add attributes to an instance at runtime using dot notation.
Example:

python
obj = Car("Tesla", "Model S")
obj.color = "Red"  # Adding a new attribute dynamically

13. How to bind attributes to objects and classes
Attributes can be bound to instances or to the class itself. Instance attributes are unique to each object, while class attributes are shared.

14. What is the __dict__ of a class and/or instance of a class and what does it contain
__dict__ is a dictionary containing all attributes and their values for an object or class.
15. How does Python find the attributes of an object or class
Python looks for attributes in the instance's __dict__ first, then in the class's __dict__, and finally in the parent classes' __dict__.

16.  How to use the getattr function
getattr(object, "attribute", default) retrieves the value of an attribute if it exists; otherwise, it returns the default value.

