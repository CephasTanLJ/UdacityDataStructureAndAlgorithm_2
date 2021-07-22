# Problem 3: Huffman coding
by Cephas Tan Li-Jie
## Assignment description
Use Huffman Coding method to encode and decode a message.

## Method of implementation
### Data Structures used:
1. Dictionary
2. Priority Queue (from `heapq`)
3. Tree/Node 
4. Stack

I stored helper data structures in the problem3_helper.py file to make reading the code easier.
The problem3.py file only contains the 2 functions `huffman_endoing()` and `huffman_decoding()`.

The sentence is first broken down into its constituent characters and stored in a dictionary (`char_dict`) 
with the characters as keys and Node(char, frequency, huffman_code) as values. This step should take O(n) to 
traverse the entire sentence, but updating the frequency of each char information node is O(1) because a dictionary 
data structure is used. At this point all the information is stored in the values (Nodes()) of the dictionary. 
The `dictionary.values()` is converted into a priority queue with the help of heapify. 
Nodes here can have arithmatic comparison because I modified the `__lt__`,`__gt__`,`__eq__` of the Node class to allow 
comparison by `self.frequency`. Using the method described in the udacity problem assignment, lower priority nodes 
(lowest frequency) are used to make internode/parent nodes; `heappop()` two child nodes at a time/step. After creating 
parent node, the parent node is reinserted into the priority queue and the entire process repeats itself until a single 
node remains in the queue. This final node becomes the root node of the Huffman binary tree. \
After the creation of the binary tree, the Huffman binary code of each nodes are derived using the help of the helper
`Stack()` data Structure class and a `State` class. The `State()` class helps to monitor if the node have been visited 
before. After the updating of the Huffman binary code for each node, the `char_dict` dictionary is re-purposed to 
contain the updated {char:Leaf_node} key:value pair. This allow quick look up of binary code for each char of the 
sentence to return the Huffman encoded string.

The decoding function is much easier because the node used to create the tree contains all the information of the char.
Given the Huffman Binary tree, the tracker_node traverse the binary tree given the an encoded string 
(0: left_child; 1: right_child), the tracker_node is re-assigned to the root of the tree everytime it reaches 
the leafNode. At each encounter with a leafNode, the leafNode`.char` is used to reconstruct the message.

### Components:
>**Functions** \
> (problem3.py file)
>>1. `huffman_encoding(data)` \
     returns: (encoded_str, huffman_tree) 
>>1. `huffman_decoding(encoded_data, tree)` \
     returns: decoded_data

>**Node** \
>  (problem3_helper.py file)
>> **Attributes**:
>> 1. `self.char` --  Character/letter.
>> 1. `self.frequency` --  Frequency of the character in the given sentence.
>> 1. `self.code` --  Huffman code associated with the node instance (derived after/from a constructed Huffman binary tree).
>> 1. `self.internode` --  Boolean: If the node instance is an internode.
>> 1. `self.root` --  Boolean: If the node instance is the root of the Huffman binary tree.
>> 1. `self.left`   
>> 1. `self.right`
> 
>> **Methods**: 
>> 1. `has_left_child()` 
>> 1. `has_right_child()` 
>> 1. `get_left_child()`
>> 1. `get_code()` -- return the huffman code of the node instance. 
>> 1. `set_code()` -- set the huffman code of the node instance.
>> 1. `get_char()` 
>> 1. `nodeType()` -- return the node type: Either a Root, Internode or leaf node.
>> 1. `set_root()` -- Only need to call once after the construction of the huffman tree. 
>> 1. `is_leafNode()` -- Check if the node in the huffman binary tree is a leaf node.
>> 1. `__add__()`-- allows the creation of a parent node of the binary tree given 2 child nodes 
      (left and right). 
>> 1. `__get__()`, `__lt__()`, `__eq__()` -- allows the arithmetic comparison 
      of Node frequency without having to call 
      for the Node.frequency attribute for every comparison.
> 
>> **Representation** \
>> Node({self.char}, {self.frequency}, {self.code}, {self.nodeType()})


>**Tree** \
>  (problem3_helper.py file)
>> **Attributes**:\
>> `self.root` --  root of the tree.
> 
>> **Methods**:\
>> `get_root()`

>**Stack** \
>  (problem3_helper.py file)
>> **Attributes**:\
>> `self.list` -- list data structure
> 
>> **Methods**: 
>> 1. `push()`
>> 1. `pop()`
>> 1. `top()`
>> 1. `is_empty()`

>**State** \
>  (problem3_helper.py file)
>> **Attributes**:
>> 1. `self.node` -- list data structure
>> 1. `self.visited_left` -- visited left child: Boolean
>> 1. `self.visited_right` -- visited right child: Boolean
> 
>> **Methods**: 
>> 1. `get_node()`
>> 1. `get_visited_left()`  -- return status of left node visit
>> 1. `get_visited_right()` -- return status of right node visit
>> 1. `set_visited_left()` -- set status of left node visit to visited (True)
>> 1. `set_visited_right()` -- set status of right node visit to visited (True)