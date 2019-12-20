from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If capacity is reached, replace oldest item with new item
        if self.storage.length == self.capacity:

            # If current item is not tail, set current value to input value
            if self.current.next:
                self.current.value = item
                # Set current as next value
                self.current = self.current.next
            # If current item is tail, set tail value as input value
            else:
                self.current.value = item
                # Set head as current value
                self.current = self.storage.head
        # If capacity is not full, add items to tail of list
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        def get_inner(node):
            if node.next is not None:
                list_buffer_contents.append(node.value)
                return get_inner(node.next)
            else:
                list_buffer_contents.append(node.value)

        get_inner(self.storage.head)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
