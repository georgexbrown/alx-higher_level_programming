#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to list to be checked (head)
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return 1;

	current = list->next;
	while (current != NULL & current != list)
		current = current->next;
	return (current == list);
}
