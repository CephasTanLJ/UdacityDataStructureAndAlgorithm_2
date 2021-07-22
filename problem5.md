# Problem 5: Block Chain 
by Cephas Tan Li-Jie
## Assignment description
Using the concept of Hashing and linkedlist data structure to make a simple block chain class.


## Method of implementation
Each element of the blockchain is a block and they are linked together via a linkedlist data structure.
The `find_block(data_message)`method in the BlockChain allows you to find and return the block in the blockchain.


>**Block Class** 
>> **Attributes**:
>> 1. `self.timestamp` -- GMT of when the block was created.
>> 1. `self.data` -- string/message of the current block.
>> 1. `self.hash` -- hash of a block's instance. 
>> 1. `self.previous_hash` -- previous hash code only. 
>> 1. `self.previous_block` -- previous block.
> 
>> **Methods**: 
>> 1. `calc_hash()` -- Hash function 
>> 1. `get_data()`  
>> 1. `get_block_hash()`  
>> 1. `get_previous_hash()`  
>> 1. `get_previous_block()`
>> 1. `set_previous_block()`
>> 1. `_set_previous_hash()`
> 
>> **Representation:**
>> ___
>> Timestamp: ...\
>> Data: ...\
>> Block Hash: ...\
>> Previous Hash: ...
>> ---

>**BlockChain Class** 
>> **Attributes**:
>> 1. `self.head` -- Where new blocks are append.
>> 1. `self.tail` -- Oldest block.
> 
>> **Methods**: 
>> 1. `append(next_block)` -- append from the`self.head`side.  
>> 1. `find_block(data_message)` -- return the block that contains the data_message. Traversed from the self.head 
      to self.tail of the linked list.
> 
>> **Representation:**\
>> Head Block 1 (newest)\
>> Block 2 \
> ...(number of blocks traversed)...\
>> Tail Block




   
