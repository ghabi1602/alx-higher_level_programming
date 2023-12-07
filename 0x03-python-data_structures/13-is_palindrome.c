#include "lists.h"

/**
 * is_palindrome: checks if the list is palindrome or not
 * @head: the head of the list
 * Return: 1 if palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *p;
	unsigned int len = 0, i;
	int *arr;

	if (*head == NULL)
		return (1);
	p = *head;

	while (p->next != NULL)
	{
		len++;
		p = p->next;
	}
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (-1);
	p = *head;
	i = -1;
	while (p != NULL)
	{
		i++;
		arr[i] = p->n;
		p = p->next;
	}
	i = 0;
	while ((arr[i] == arr[len]) && (len > i))
	{
		i++;
		len--;
	}
	free(arr);
	if (i >= len)
		return (1);
	return (0);
}
