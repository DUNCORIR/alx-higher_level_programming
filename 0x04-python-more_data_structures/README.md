0x04. Python - More Data Structures: Set, Dictionary
0. Sets in Python
A set is an unordered collection of unique elements. They are commonly used when you need to store unique items and perform set operations like union, intersection, difference, etc.

Key Points:
No duplicates: A set automatically removes duplicate elements.
Unordered: The elements in a set do not have a fixed order.
Mutable: You can add or remove elements.
Methods: add(), remove(), union(), intersection(), difference(), etc.
Common Methods:
add(elem): Adds an element to the set.
remove(elem): Removes an element from the set, raises an error if not found.
discard(elem): Removes an element, but does nothing if the element is not present.
union(set1, set2): Returns a set containing all elements from both sets (no duplicates).
intersection(set1, set2): Returns a set containing only elements found in both sets.
difference(set1, set2): Returns elements that are in the first set but not in the second.

1. Dictionaries in Python
A dictionary is an unordered collection of key-value pairs. It allows for fast lookup, insertion, and deletion based on a unique key.

Key Points:
Key-Value pairs: Each element consists of a key and a value.
Keys are unique: You can’t have duplicate keys.
Keys must be immutable: For example, numbers, strings, or tuples can be used as keys.
Values can be anything: They can be any data type, even another dictionary.
Common Methods:
dict.get(key): Returns the value for the given key; returns None if the key doesn’t exist.
dict.items(): Returns a view object of key-value pairs.
dict.keys(): Returns a view object of all keys.
dict.values(): Returns a view object of all values.
dict.update(other_dict): Merges other_dict into the current dictionary.
dict.pop(key): Removes the key-value pair and returns the value
