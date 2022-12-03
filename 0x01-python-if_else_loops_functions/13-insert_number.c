#include "lists.h"

/**
 * insert_node - Write a function in C that inserts a
 * number into a sorted singly linked list.
 * @head: head
 * @number: number to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *next = *head, *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	while (next)
	{
		if (next->n > number)
			break;
		current = next;
		next = next->next;
	}

	node->n = number;

	if (*head == NULL)
	{
		node->next = NULL;
		return (*head = node);
	}

	if (next == *head)
	{
		node->next = *head;
		return (*head = node);
	}

	node->next = next;
	current->next = node;

	return (node);
}
