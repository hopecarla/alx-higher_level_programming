#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there's no cycle, 1 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	if (list == NULL || list->next == NULL)
		return(0);
	slow_ptr = list;
	fast_ptr = list->next;

	while (fast_ptr != NULL && fast_ptr->next  != NULL)
	{
		if (slow_ptr == fast_ptr)
			return (1);
		slow_ptr = slow_ptr->next;
	slow_ptr = fast_ptr->next->next;
	}
	return (0);
}
