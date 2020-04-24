from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.current.value = item
            if self.current.next is None:
                self.current = self.storage.head
            else:
                self.current = self.current.next

        elif len(self.storage) == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        else:
            self.storage.add_to_tail(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        curr = self.storage.head
        while(curr):
            list_buffer_contents.append(curr.value)
            curr = curr.next
        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
