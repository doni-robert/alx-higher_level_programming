#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a singly linked list
 * @head: pointer to head of the list
 * @number: number to be inserted
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *previous;

	current = *head;
	new_node = malloc(sizeof(listint_t));

	while (current->next != NULL)
	{
		if (current->n < number)
		{
			previous = current;
			current = current->next;
		}
		else
		{
			new_node->n = number;
			new_node->next = current;
			previous->next = new_node;

			break;
		}
	}
	return (new_node);
}
