# Problem 6: Union and Intersection of Two Linked Lists
by Cephas Tan Li-Jie
## Assignment description
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B 
is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted 
by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of 
either the union or intersection, respectively. Once you have completed the problem you will create your own test cases 
and perform your own run time analysis on the code.

## Method of implementation
Create a new linkedList (`new_ll`).\
\
**For union function:**\
Traverse the first linkedlist and add unique values (`Node.value`) to a python sets() datatype.
Check if each node of the linkedList exists within the unique values set. If they are not present in the unique set, 
append a new node with the unique value to the `new_ll`. If they are already present in the `unique_values`set, it means
they are not unique and can be ignored. After traversing the first linkedlist, continue to the second linked list and 
repeat the process using the existing `unique_values` set. The final linked list will contain unique values that are 
elements values that can be found in either the first and/or the second linked list.\
Overall, the new linkedList is created as we traverse through each linked list. Therefore, the time complexity 
for this function is O(n), whereby n is the sum of elements/nodes of both linked list.

**For intersection function**\
Traverse the first linkedList and add unique values (`Node.value`) to a python sets() datatype.
Traverse the second LinkedList and Check if each node of the linkedList exists within the unique values set.
If they are already present in the `unique_values`set, it means they are intersecting elements of both linkedlist. 
Add them to the `new_ll` and remove existing values from the set to indicate that the `new_ll` 
already contains the element. If they are not present in the `unique_values` set, they are not elements of both 
linked list and can be ignored.\
Overall, alike the union function, new linkedList is created as we traverse through each linked list. Therefore, the
time complexity is also O(n).


>**Functions** 
>>1. `union(llist1, llist_2)`
>>1. `intersection(llist1, llist2)`
> 

>**Node Class** 
>> **Attributes**:
>> 1. `self.value`
>> 1. `self.next`
>

>**LinkedList Class** 
>> **Attributes**:
>> 1. `self.head` 
> 
>> **Methods**: 
>> 1. `append(value)` 
>> 1. `size()` -- return the size of the linked list





   
