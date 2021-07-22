class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist1, llist_2):
    new_ll = LinkedList()
    unique_values = set()

    # Traverse llist1
    tracker_node = llist1.head
    while tracker_node is not None:
        if tracker_node.value not in unique_values:
            unique_values.add(tracker_node.value)
            new_ll.append(tracker_node.value)
        tracker_node = tracker_node.next

    # Traverse llist2
    tracker_node = llist_2.head
    while tracker_node is not None:
        if tracker_node.value not in unique_values:
            unique_values.add(tracker_node.value)
            new_ll.append(tracker_node.value)
        tracker_node = tracker_node.next

    return new_ll

def intersection(llist1, llist2):
    new_ll = LinkedList()
    unique_values = set()

    # Traverse llist1
    tracker_node = llist1.head
    while tracker_node is not None:
        if tracker_node.value not in unique_values:
            unique_values.add(tracker_node.value)
        tracker_node = tracker_node.next

    # Traverse llist1 and look out for intersecting values
    tracker_node = llist2.head
    while tracker_node is not None:
        if tracker_node.value in unique_values:
            unique_values.remove(tracker_node.value)    # To prevent appending of same values
            new_ll.append(tracker_node.value)
        tracker_node = tracker_node.next

    if new_ll.size() == 0:
        return None

    return new_ll

def test():
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))

if __name__ == '__main__':
    test()