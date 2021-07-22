# Problem 1: Least Recently Used (LRU) Cache
by Cephas Tan Li-Jie
## Assignment description
Create a LRU Cache with operators taking O(1) time.

## Method of implementation
### Data Structures used:
1. Dictionary
2. Queue (from `collections.deque`) 

I used the python's base::dictionary data structure as the cache. 
This is because it allows me to look up key:value pairs in O(1).
I used deque from python collections module to allow me to "monitor" and identify 
the "age" of the keys, for the FIFO method of clearing the cache to insert new key. 
Using a queue data structure allows me to `pop()` out the oldest used key in the cache to
make space to insert a newer key (that was not already in the cache). For items already
present in the cache, the "age" status is renewed in the queue data structure.

### Components:
>**LRU_Cache Class**
>> **Attributes**:
>> 1. `self.capacity` -- Size of the cache; deafault is 5.
>> 2. `self.current_load` -- Current number of "objects" in the cache.
>> 3. `self.cache` -- The cache using a dictionary datastructure.
>> 4. `self.queue` -- A queue datastrcuture used to monitor the age of the objects in the cache.
> 
>> **Methods**:
>> 1. `get(key)` -- return the value of the key in the cache. returns -1 when key:value pair not in cache.
>> 1. `set(key, value)` -- Add a key:value pair into cache or update the key:value "age" in the cache.
>> 1. `_removeOldestKey()` -- \Remove the oldest key within the cache.
>> \* _methods() are hidden methods to prevent users from accidentally using it.
> 
>> **Representation** \
>> The LRU_cache class is represented as a list of the cache with the 1st element being the newest(left-most element) 
>> and the last element (right-most element) being the oldest.

   



