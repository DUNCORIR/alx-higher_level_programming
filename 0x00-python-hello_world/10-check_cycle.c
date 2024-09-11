#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: A pointer to the head of the list.
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	/* Edge case: If the list is empty, there is no cycle */
	if (list == NULL)
		return (0);

	/* Initialize two pointers */
	slow = list; /* The slow pointer will move one step at a time */
	fast = list; /* The fast pointer will move two steps at a time */

	/* Traverse the list with two pointers */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next; /* Move the slow pointer one step */
		fast = fast->next->next; /* Move the fast pointer two steps */

		/* If the slow pointer and fast pointer meet, a cycle is detected */
		if (slow == fast)
			return (1);
	}
	/* we reach here, the fast pointer has reached the end of the list */
	return (0);
}
