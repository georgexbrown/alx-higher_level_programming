#include "lists.h"

/**
 * reverse_list - function that reverses the singly linked list
 * @head: pointer to the list (head node)
 *
 * Return: pointer to the first node (head node)
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - function that checks if a singly linked list is palindrome
 * @head: pointer to the list (head node)
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head, *second = *head;
	listint_t *temp = *head, *current = NULL;

	if (!(*head) || !((*head)->next))
		return (1);

	while (1)
	{
		first = first->next->next;
		if (!first)
		{
			current = second->next;
			break;
		}
		if (!first->next)
		{
			current = second->next->next;
			break;
		}
		second = second->next;
	}

	reverse_list(&current);

	while (current && temp)
	{
		if (temp->n == current->n)
		{
			current = current->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!current)
		return (1);

	return (0);
}
