#include "lists.h"
/**
 * insert_node: inserst node in a sorted lists
 * @head: head of the list
 * @number: node to be inserted
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;
	
	if (head == NULL)
	{
		return (NULL);
	}	
	temp = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (temp->n > number)
	{
		*head = new;
		new->next = temp;
	}
	while (temp->next != NULL)
	{
		if(temp->next->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	temp->next = new;
	return (new);
}
