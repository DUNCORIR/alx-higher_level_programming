#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: number to insert in the list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t)); /* Allocate memory for the new node */
	if (new_node == NULL)
		return (NULL);

	new_node->n = number; /* Assign the number to the new node */
	new_node->next = NULL;

	/* Case 1: The list is empty or number should be inserted at the start */
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head; /* New node points to current head */
		*head = new_node;       /* New node becomes the new head */
		return (new_node);
	}
	/* Case 2: Traverse the list to find the insertion point */
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next; /* Move to the next node */
	}
	/* Insert the new node */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
