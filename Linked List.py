class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_last(self):
        temp = self.head
        pre = self.head
        if temp is None:
            return "Linked List is empty"
        else:
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if temp is None:
            return "Linked List is empty"
        else:
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        temp = self.head
        if index < 0 or index > self.length:
            return None
        else:
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        return True 

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first(index)
        elif index == self.length - 1:
            return self.pop_last(index)
        else:
            pre = self.get(index-1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
        if self.length == 1:
            self.head = None
            self.tail = None
        self.length -= 1
        return temp 

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linkedList = LinkedList(1)
my_linkedList.append(2)
my_linkedList.append(3)
my_linkedList.append(4)

my_linkedList.reverse()

my_linkedList.print_list()