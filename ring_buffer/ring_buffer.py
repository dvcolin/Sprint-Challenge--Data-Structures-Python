from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If capacity is reached, replace oldest item with new item and shift items over
        self.current = self.storage.head
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            pass

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
