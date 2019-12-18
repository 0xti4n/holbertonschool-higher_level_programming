#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* add_nodeint - Add new node at the beginning of a list.
* @head: The argument.
* @n: The data.
* Return: The new node.
*/

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = n;
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}

/**
*is_palindrome - find palindrome
*@head: The list.
*Return: 1 if id palindrome 0 if not.
*/

int is_palindrome(listint_t **head)
{
	listint_t *new_r, *temp;

	if (head)
	{
		if (*head == NULL)
			return (1);
		temp = *head;
		new_r = NULL;
		while (temp)
		{
			add_nodeint(&new_r, temp->n);
			temp = temp->next;
		}
		while (rev && *head != NULL)
		{
			if ((*head)->n == rev->n)
			{
				rev = rev->next;
				*head = (*head)->next;
			}
			else
				return (0);
		}
		return (1);
	}
	return (0);
}
