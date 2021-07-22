# Problem 4: Active Directory 
by Cephas Tan Li-Jie
## Assignment description
Write a function that provides an efficient look up of whether the user is in a group.
given that the Group class uses a python list to store the information.

## Method of implementation
Using a recursive method similar to problem 2 (file recursion) to unveal the given group and the check if the user 
is a member.

>**Functions** 
>>`is_user_in_group(user, group)` --
>>  Recursive function used to find the membership group(s) of the given user.

>**Group Class** 
>> **Attributes**:
>> 1. `self.name` -- Name of this `Group()` class
>> 1. `self.groups` -- `Group()` classes membership.
>> 1. `self.users` -- Names/ID of users within this `Group()`instance

> 
>> **Methods**: 
>> 1. `add_group()` 
>> 1. `add_user()` 
>> 1. `get_group()` 
>> 1. `get_users()` 
>> 1. `get_name()`
> 
>> **Representation** \
>> f'Name: {self.name} Group: {self.groups} Users: {self.users}'




   
