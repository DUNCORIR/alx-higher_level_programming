0x02. Python - import & modules
This project introduces key concepts in Python programming related to modules, importing functions, and command line arguments.
1. Import Functions from Another File
Can import the entire module using import mymodule and access functions as mymodule.add(5, 3).

2. Use Imported Functions
Once you import a function, you can call it as if it were defined in the same file

#Example 

from mymodule import add

result = add(10, 20)
print(result)  # Output: 30

3. Create a Module
A module in Python is simply a file that contains Python code (e.g., mymodule.py). You can create a module by writing any Python file with functions, variables, or classes that you want to reuse in other programs.

4. Use the Built-in Function dir()
The dir() function returns a list of valid attributes for an object, including functions, variables, and classes within a module. It’s a useful tool for inspecting the content of a module.

5. Prevent Code in Your Script from Being Executed When Imported
When you import a module, Python executes all the code in that file. To prevent some code from running when the module is imported, you can use the __name__ == "__main__" check.Example:
# mymodule.py
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()
In this case, the greet() function will only run if the file is executed directly, but it will not run if mymodule.py is imported into another file.

6. Use Command Line Arguments with Your Python Programs
Python provides access to command line arguments through the sys.argv list, where argv[0] is the name of the script and the subsequent elements are the arguments passed to the script

#Summary
Here’s a recap of what we’ve covered:

Python is awesome because it’s simple, versatile, and widely used.
Import functions from other files using import or from ... import ....
Use imported functions by calling them directly.
Create a module by writing a Python file with reusable functions or classes.
Use the dir() function to inspect modules and variables.
Prevent code execution on import by wrapping it in if __name__ == "__main__".
Use command-line arguments via sys.argv.
