from heapq import heapify, heappush, heappop
from problem3_helper import Node, State, Stack, Tree
import sys


def huffman_encoding(data):
    # Creating dictionary of char {"A": Node('A', char_freq, binary_code, node_type) }
    data = str(data)

    # Edge case for data = '' or None
    if len(data) == 0 or data == 'None':
        raise ValueError('The data is an empty string')

    # Continue for normal cases
    char_dict = dict()
    for char in data:
        if char not in char_dict:
            char_dict[char] = Node(char, 1)
        else:
            char_dict[char].frequency += 1

    # Edge case when only 1 char type exists e.g., 'AAAAAAA', it should return 0000000 as code and Node('A',freq=7,code=None,Leaf)
    encoded_str = ''
    if len(char_dict) == 1:
        for _ in data:
            encoded_str = f'{encoded_str}0'

        char = data[0]
        huffman_tree = Tree(char_dict[char])
        return encoded_str, huffman_tree

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

    # To decode edge case whereby encoded("AAAAAAA") is "0000000"
    if tree.root.is_leafNode():
        char = tree.root.get_char()
        for binary_code in encoded_data:
            message = f'{message}{char}'
        return message


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


def test():
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    # Assertion Test to see if there is an improvement in terms of size after Huffman compression
    assert sys.getsizeof(int(encoded_data, base=2)) < sys.getsizeof(a_great_sentence), "The Compression did not reduce the size!"

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Assertion test to ensure no lost of information after encoding then decoding.
    assert sys.getsizeof(decoded_data) == sys.getsizeof(a_great_sentence), "There is a loss of information after compression"
    assert huffman_decoding(*huffman_encoding(a_great_sentence))== a_great_sentence, "Did not encode and decode correctly."

def test2():
    edge_sentence = 'AAAAAAA'
    encoded_str, tree = huffman_encoding(edge_sentence)

    assert encoded_str == '0000000', f'The encoded string for "AAAAAAA" should be "0000000", but {encoded_str} was returned.'
    assert tree.root == Node('A',7), f'The huffman tree.root should be "Node(A,7,None,Leaf)", but {tree.root} was returned.'

    assert huffman_decoding(encoded_str, tree) == 'AAAAAAA', f'decoding should return "AAAAAAA" but {huffman_decoding(encoded_str, tree)} was returned.'


def test3():
    '''Test if empty edge case raises the ValueError.'''
    try:
        empty_sentence = ''
        encoded_str, tree = huffman_encoding(empty_sentence)
        assert 'encoded_str' not in locals(),"test3: No encoded string should be generated, and and a ValueError should be raised for empty strings."
        assert 'tree' not in locals(),"test3: No tree should be generated, and and a ValueError should be raised for empty strings."
    except ValueError:
        print('ValueError was successfully raised for empty sentence data input test3')

def test4():
    '''Test if None data edge case raises the ValueError.'''
    try:
        encoded_str, tree = huffman_encoding(None)
        assert 'encoded_str' not in locals(),"test4: No encoded string should be generated, and and a ValueError should be raised for None data."
        assert 'tree' not in locals(),"test4: No tree should be generated, and and a ValueError should be raised for None data."
    except ValueError:
        print('ValueError was successfully/correctly raised for empty sentence data input test4')


if __name__ == '__main__':
    test()
    test2()
    test3()
    test4()
    print('tests done')