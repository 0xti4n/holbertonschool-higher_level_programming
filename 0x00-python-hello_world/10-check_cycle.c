#include "lists.h"

/**
* check_cycle - Checks if a singly linked list has a cycle in it.
* @list: the node.
* Return: 0 if it has no cycle, otherwise 1.
*/

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	while (a && a->next && b != NULL)
	{
		a = a->next->next;
		b = b->next;

		if (a == b)
		{
			return (1);
		}
	}
	return (0);
}
