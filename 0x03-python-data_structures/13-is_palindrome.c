#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 *
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next; /* Store the next node */
		current->next = prev; /* Reverse the current node's pointer */
		prev = current;       /* Move prev to current node */
		current = next;       /* Move to the next node */
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half = NULL;
	listint_t *first_half = *head, *prev_of_slow = NULL, *mid = NULL;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL) /* check for empty list */
		return (1);
	while (fast != NULL && fast->next != NULL) /* find middle of list */
	{
		fast = fast->next->next;   /* Move fast pointer two steps */
		prev_of_slow = slow;       /* Save the node before the middle */
		slow = slow->next;         /* Move slow pointer one step */
	}
	if (fast != NULL) /* skip the middle element */
	{
		mid = slow;
		slow = slow->next;
	}
	second_half = reverse_list(slow); /* Reverse the second half of the list */
	prev_of_slow->next = second_half;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			result = 0;    /* Not a palindrome */
			break;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	if (mid != NULL) /* Restore the list to its original state */
	{
		prev_of_slow->next = reverse_list(second_half);
		mid->next = prev_of_slow->next;
	}
	else
	{
		prev_of_slow->next = reverse_list(second_half);
	}
	return (result); /* Return the result: 1 if palindrome, 0 otherwise */
}
