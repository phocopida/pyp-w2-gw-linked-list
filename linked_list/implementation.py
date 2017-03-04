from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList interface.
    """

    def __init__(self, elements=None):
        
        
        self.start = None
        self.end = None
        
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        if not self.start:
            return "[]"
        else:
            a = [elems for elems in self]
            return "{}".format(a)

    def __len__(self):
        return self.count()

    def __iter__(self):
        current_node = self.start
        while current_node:
            yield current_node.elem
            current_node = current_node.next
        raise StopIteration

    def __getitem__(self, index):
        if not self.start or index >= len(self):
            raise IndexError
        for num, item in enumerate(self):
            if num == index:
                return item

    def __add__(self, other):
        sum_list = LinkedList([elem for elem in self])
        for elem in other:
            sum_list.append(elem)
        return sum_list

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        
        return self

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        current1 = self.start
        current2 = other.start
        
        if not current1 and not current2:
            return True
        if not bool(current1) or not bool(current2):
            return False
        if len(self) != len(other):
            return False
        while current1.next:
            if current1 == current2:
                current1 = current1.next
                current2 = current2.next
            else:
                return False
        return True

    def append(self, elem):
        if not self.start:
            self.start = Node(elem)
            self.end = self.start
            return self.start
            
        new = Node(elem)
        self.end.next = new
        self.end = new
        return self.end

    def count(self):
        count_no = 0
        if not self.start:
            return count_no
        current_node = self.start
        while current_node:
            count_no+=1
            current_node = current_node.next
        return count_no 

    def pop(self, index=None):
        if len(self) == 0:
            raise IndexError
        if index == None:
            index = len(self)-1
        if index >= len(self):
            raise IndexError
        if index == 0:
            return_elem = self.start.elem
            self.start = self.start.next
            return return_elem
        if index > 0:
            prev_node = None
            current_node = self.start
            count = 0
            while current_node:
                count += 1
                prev_node = current_node
                current_node = current_node.next
                if count == index:
                    return_elem = current_node.elem
                    prev_node.next = current_node.next
                    return return_elem    
