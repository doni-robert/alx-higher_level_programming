#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: the singly linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	int i, n = 0;
	listint_t *temp, *current;

	current = list;
	while (current->next != NULL)
	{
		current = current->next;
		n++;
		
		temp = list;
		for (i = 0; i <= n; i++)
		{
			if (current->next == temp)
				return (1);
			temp = temp->next;
		}
	}
	return (0);
}
