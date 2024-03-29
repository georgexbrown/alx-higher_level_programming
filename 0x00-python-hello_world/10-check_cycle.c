#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to list to be checked (head)
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = first;

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
		{
			first = list;
			while (first && second)
			{
				if (first == second)
					return (1);
				first = first->next;
				second = second->next;
			}
		}
	}
	return (0);
}
