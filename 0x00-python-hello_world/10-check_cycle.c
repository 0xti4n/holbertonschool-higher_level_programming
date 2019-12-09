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

	while (a && b != NULL)
	{
		if (a->next->next == b->next)
		{
			return (1);
		}
		a = a->next->next;
		b = b->next;
	}
	return (0);
}
