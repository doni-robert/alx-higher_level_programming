#!/usr/bin/python3
"""Defines a class Node of a singly linked list class"""


class Node:
    """A class to represent a node"""

    def __init__(self, data, next_node=None):
        """
        Initializes a new node

        Args:
            data(int): The data of the new node
            next_node(node): The next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the current data of a node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Get the current next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a class SinglyLinkedList"""


class SinglyLinkedList:
    """Represents a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list

        Args:
            value: The new node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """The print representation of the list"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
