#include "lists.h"

/**
 * reverse - reverse a singly linked list
 *
 * @head: list
 */
void reverse(listint_t **head)
{
	listint_t *prev, *current, *next;

	prev = NULL, current = *head;
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
 * compare - compare two singly linked list
 * @h1: first head
 * @h2: second head
 * Return: 1 if h1 and h2 are shallowly equal
 * otherwise 0
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *temp1 = h1;
	listint_t *temp2 = h2;

	while (temp1 && temp2)
	{
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a
 * palindrome
 *
 * @head: head of the linked list
 * Return: 1 if list is a palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *half;
	listint_t *mid, *prevslow;
	int ispalindrome = 1;

	slow = fast = *head;
	mid = NULL;
	if (*head && (*head)->next)
	{
		while (fast && fast->next)
		{
			fast = fast->next->next;
			prevslow = slow;
			slow = slow->next;
		}
		if (fast)
		{
			mid = slow;
			slow = slow->next;
		}
		half = slow;
		prevslow->next = NULL;
		reverse(&half);
		ispalindrome = compare(*head, half);

		reverse(&half);
		if (mid)
		{
			prevslow->next = mid;
			mid->next = half;
		}
		else
		{
			prevslow->next = half;
		}
	}
	return (ispalindrome);
}
