from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Check if ring buffer is at max capacity
        if self.storage.length == self.capacity:

            # If so, set the value of self.current to be item
            self.current.value = item

            # If self.current is not the tail, set self.current to be the next node
            if self.current.next != None:
                self.current = self.current.next
            # Else, set self.current to be the head node
            else:
                self.current = self.storage.head
        # If buffer is not at capacity, add the item to the tail and set self.current to be the head node
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_item = self.storage.head
        while current_item != None:
            list_buffer_contents.append(current_item.value)
            current_item = current_item.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
