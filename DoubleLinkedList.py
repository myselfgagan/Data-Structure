from typing import Text


class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_last(self):
        temp = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None  
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        temp = self.head
        if index < 0 or index > self.length:
            return None
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index-1)
            after = before.next
            before.next = new_node
            new_node.next = after
            after.prev = new_node
            new_node.prev = before

    def remove(self, index):
        temp = self.get(index)
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop_last()
        else:
            before = temp.prev
            after = temp.next
            before.next = after
            after.prev = before
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

my_dll = DLL(1)
my_dll.append(2)
my_dll.append(3)

my_dll.remove(0)
my_dll.print_list() 