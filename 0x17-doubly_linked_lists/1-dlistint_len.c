#include "lists.h"

/**
 * dlistint_len - Function that returns number of
 * elements in doubly linked lists
 * @h: pointer to head of doubly linked lists.
 *
 * Return: The number of elements in a doubly linked lists.
 */
size_t dlistint_len(const dlistint_t *h)
{
	/* Initialize counter for number of nodes.*/
	size_t node_count = 0;

	/* Traverse list starting from head */
	while (h != NULL)
	{
		/* Increment the node conter for each node visited */
		node_count = node_count + 1; /* or node_count++; */
		h = h->next;
	}
	/* Return total number of nodes */
	return (node_count);
}
