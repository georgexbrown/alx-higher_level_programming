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
