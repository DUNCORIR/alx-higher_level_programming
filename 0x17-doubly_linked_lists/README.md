0x17. C - Doubly linked lists
A doubly linked list (DLL) in C is a structure where each node contains three parts: the data, a pointer to the next node, and a pointer to the previous node.

This creates the basic structure for a DLL node. Each node contains an integer (data) and pointers to the next (next) and previous (prev) nodes.

Key Operations on Doubly Linked Lists in C
Insertion:

Inserting at the beginning.
Inserting at the end.
Inserting after a specific node.
Deletion:

Deleting a node from the beginning.
Deleting a node from the end.
Deleting a specific node.
Traversal:

Traversing forward.
Traversing backward.

Deleting a Node in a DLL
To delete a node, you need to adjust the prev and next pointers of the surrounding nodes.

Traversing the DLL
Forward Traversal: Start from the head and use the next pointers.
Backward Traversal: Start from the tail and use the prev pointers.

To perform backward traversal, you need to first reach the last node and then traverse using the prev pointers.


