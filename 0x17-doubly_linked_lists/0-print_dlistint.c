#include "lists.h"

/**
 * print_dlistint - prints all elements of dlistint_t list
 * @h: Pointer to the head of doubly linked list.
 *
 * Return: The number of nodes in the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t node_count = 0;

	/* Traverse the list from head to end */
	while (h != NULL)
	{
		printf("%d\n", h->n); /* n is data field in dlistint_t*/
		/* Increment the node counter */
		node_count++;
		h = h->next;
	}
	/* Return total number of nodes*/
	return (node_count);
}
