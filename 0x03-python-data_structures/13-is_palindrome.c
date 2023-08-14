#include "lists.h"

/**
 * reverse_linked_list - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next_node = NULL;

	while (current)
	{
		next_node = current->next;
		current->next = previous;
		previous = current;
		current = next_node;
	}

	*head = previous;
}

/**
 * is_linked_list_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortoise = *head, *hare = *head, *current_node = *head, *reversed_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		hare = hare->next->next;
		if (!hare)
		{
			reversed_half = tortoise->next;
			break;
		}
		if (!hare->next)
		{
			reversed_half = tortoise->next->next;
			break;
		}
		tortoise = tortoise->next;
	}

	reverse_listint(&reversed_half);


	while (reversed_half && current_node)
	{
		if (current_node->n == reversed_half->n)
		{
			reversed_half = reversed_half->next;
			current_node = current_node->next;
		}
		else
			return (0);
	}

	if (!reversed_half)
		return (1);

	return (0);
}

