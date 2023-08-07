#include "lists.h"

/**
 * check_cycle - checks for cycle in a linked list
 * @list: linked list
 *
 * Return: linked list has cycle 1 else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (!list)
		return (0);
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}

	return (0);
}
