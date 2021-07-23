class Node:
    def __init__(self, char, frequency, internode = False, root=False, left = None, right = None):
        self.char = char
        self.frequency = frequency
        self.code = None
        self.internode = internode
        self.root = root
        self.left = left
        self.right = right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_code(self):
        return self.code

    def set_code(self, binaryCodeSeq):
        '''
        prefix_binaryCode = 0 for left child,
        prefix_binaryCode = 1 for right child.
        '''
        self.code = f'{binaryCodeSeq}'

    def get_char(self):
        return self.char

    def nodeType(self):
        if self.root is True:
            return 'Root'
        elif self.internode is False and self.root is False:
            return 'Leaf'
        elif self.internode is True:
            return 'Internode'

    def set_root(self):
        self.root = True

    def is_leafNode(self):
        return self.internode is False and self.root is False

    def __add__(self, other):
        char = self.char + other.char
        frequency = self.frequency + other.frequency
        return Node(char, frequency, internode=True, left=self, right=other)

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __repr__(self):
        return f'Node("{self.char}", {self.frequency}, {self.code}, {self.nodeType()})'

class Tree:
    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root

class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

class State:
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True
