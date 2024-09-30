0x05. Python - Exceptions
1. What’s the difference between errors and exceptions:

Errors: Problems in the code that prevent it from running, like syntax errors.
Exceptions: Issues that arise during execution, even if the code syntax is correct.

2. What are exceptions and how to use them: Exceptions are events that disrupt normal program flow. You handle them using try and except blocks.

3. When do we need to use exceptions: Use exceptions to handle unforeseen errors (e.g., invalid user input, file not found) gracefully without crashing the program.

4. How to correctly handle an exception: Use try blocks to test code that might raise an exception and except blocks to define what happens when an exception occurs.

5. What’s the purpose of catching exceptions: Catching exceptions prevents the program from crashing and allows you to manage errors, provide user feedback, or take corrective actions.

6. How to raise a builtin exception: You can use the raise keyword to manually trigger exceptions, e.g., raise ValueError("Invalid input").

7. When do we need to implement a clean-up action after an exception: Use the finally block to perform clean-up actions (e.g., closing files, releasing resources) that should happen whether an exception occurs or not.
