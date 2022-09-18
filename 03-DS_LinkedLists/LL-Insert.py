import re
from readline import insert_text
from tempfile import tempdir


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
        append_node = Node(value)
        if self.head is None:
            self.head = append_node
            self.tail = append_node
        else:
            self.tail.next = append_node
            self.tail = append_node 

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        prepend_node = Node(value)
        if self.length == 0:
            self.head = prepend_node
            self.tail = prepend_node
        else:
            prepend_node.next = self.head
            self.head = prepend_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
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
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.length += 1
            return self.prepend(value)
        if index == self.length:
            self.length += 1
            return self.append(value)
        insert_node = Node(value)
        temp = self.get(index-1)
        insert_node.next = temp.next
        temp.next = insert_node
        self.length += 1
        return True


my_linked_list = LinkedList(0)
my_linked_list.append(2)
my_linked_list.print_list()
my_linked_list.insert(1,1)
my_linked_list.print_list()


