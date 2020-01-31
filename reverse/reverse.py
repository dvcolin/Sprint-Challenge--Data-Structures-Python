class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        if not self.head:
            return None
        starting_node = self.head
        while starting_node.next_node != None:
            current_node = starting_node.next_node
            self.add_to_head(current_node.value)
            starting_node = starting_node.next_node
        # def reverse_list_inner(node):
        #     # If list is empty, return None
        #     if not self.head:
        #         return None
        #     # While there is a next node, add the current node to head and recurse the function
        #     else:
        #         if node.get_next() != None:
        #             self.add_to_head(node.value)
        #             return reverse_list_inner(node.next_node)
        #     # Once we are at the tail, add that node to head
        #         self.add_to_head(node.value)
        # return reverse_list_inner(self.head)
