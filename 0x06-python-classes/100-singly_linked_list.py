#!/usr/bin/python3
""" yoho Singly linked lis"""


class Node:
    """defines  node ofsingly linked list"""

    def __init__(self, data, next_node=None) -> None:
        """ initializerr"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getterr"""
        return self.__data

    @data.setter
    def data(self, value):
        """ settrer"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getterr"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setterr"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ singly linked list classs"""

    def __init__(self):
        """ initializations"""
        self.myhead = None

    def __str__(self):
        """ make a list printablee"""
        my_all_data = ""
        tempraire = self.myhead
        while (tempraire):
            my_all_data += str(tempraire.data) + "\n"
            tempraire = tempraire.next_node
        # return all data except the new line at the end
        return my_all_data[:-1]

    def sorted_insert(self, value):
        """ insert into correcttd sorted positionn"""
        myNewNode = Node(value)
        tempo = self.myhead
        if tempo is None:
            self.myhead = myNewNode
            return
        if value < tempo.data:
            myNewNode.next_node = self.myhead
            self.myhead = myNewNode
            return

        while (tempo.next_node and tempo.next_node.data < value):
            tempo = tempo.next_node
        myNewNode.next_node = tempo.next_node
        tempo.next_node = myNewNode
