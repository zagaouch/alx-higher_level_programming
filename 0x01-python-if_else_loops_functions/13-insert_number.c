#include "lists.h"
int my_index(listint_t *head, int number)
{
	int i = 0;
	
	while(head != NULL && head->n < number)
	{
		i++;
		head = head->next;
	}
	return (i);
}


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head;
	int i, index;
	
	new = malloc(sizeof(listint_t));
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		temp = *head;
		index = my_index(*head, number);
		for (i = 0; i < index - 1; i++)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}	
