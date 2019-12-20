from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If capacity is reached, replace oldest item with new item
        if self.storage.length == self.capacity:
            if self.current.next:
                self.current.value = item
                self.current = self.current.next
            else:
                self.current.value = item
                self.current = self.storage.head
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
