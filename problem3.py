from heapq import heapify, heappush, heappop
from problem3_helper import Node, State, Stack, Tree
import sys


def huffman_encoding(data):
    # Creating dictionary of char {"A": Node('A', char_freq, binary_code, node_type) }
    char_dict = dict()
    for char in data:
        if char not in char_dict:
            char_dict[char] = Node(char, 1)
        else:
            char_dict[char].frequency += 1

    # Priority Queue
    priority_queue = list(char_dict.values())
    heapify(priority_queue)

    while len(priority_queue) != 1:
        leftNode = heappop(priority_queue)
        rightNode = heappop(priority_queue)

        # My Node class allows you to "add" nodes together to become an "internode".
        interNode = leftNode + rightNode
        interNode.internode = True  # UpdateNode type
        heappush(priority_queue, interNode)

    root_node = priority_queue[0]
    root_node.set_root()  # UpdateNode Type to root
    huffman_tree = Tree(root_node)

    # Updating the char_dict using stack dataStructure
    stack = Stack()

    tracker_node = huffman_tree.get_root()
    state = State(tracker_node)
    stack.push(state)

    ## Deriving the Huffman code for each Node.
    while tracker_node is not None:
        if tracker_node.is_leafNode():
            char_dict[tracker_node.char] = tracker_node
        if tracker_node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            binary_code_prefix = tracker_node.get_code()

            tracker_node = tracker_node.get_left_child()

            if binary_code_prefix is None:
                binary_code_prefix = '0'
            else:
                binary_code_prefix = f'{binary_code_prefix}0'
            tracker_node.set_code(binary_code_prefix)

            state = State(tracker_node)
            stack.push(state)

        elif tracker_node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            binary_code_prefix = tracker_node.get_code()
            tracker_node = tracker_node.get_right_child()

            # Assigning huffman code for the node
            if binary_code_prefix is None:
                binary_code_prefix = '1'
            else:
                binary_code_prefix = f'{binary_code_prefix}1'
            tracker_node.set_code(binary_code_prefix)

            state = State(tracker_node)
            stack.push(state)

        else:
            stack.pop()
            if stack.is_empty():
                tracker_node = None
            else:
                state = stack.top()
                tracker_node = state.get_node()

    encoded_str = ''
    for char in data:
        encoded_str = encoded_str + char_dict[char].code

    return encoded_str, huffman_tree


def huffman_decoding(encoded_data, tree):
    message = str()

    tracker_node = tree.root
    for binary_digit in encoded_data:
        if binary_digit == '0':
            tracker_node = tracker_node.get_left_child()
        elif binary_digit == '1':
            tracker_node = tracker_node.get_right_child()

        if tracker_node.is_leafNode():
            message = f'{message}{tracker_node.get_char()}'
            tracker_node = tree.get_root()

    return message


if __name__ == '__main__':
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    encoded_data, tree = huffman_encoding('Yeah Booooooeeeeiii')
    print(huffman_decoding(encoded_data, tree))
