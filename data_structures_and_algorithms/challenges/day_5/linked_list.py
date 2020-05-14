from data_structures_and_algorithms.challenges.day_5.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, key):
        current = self.head
        while current:
            if current.value == key:
                return True
            current = current.next_node
        return False

    def __str__(self):
        current = self.head
        values = '\"'
        while current:
            values += f'{{ {current.value} }} -> '
            current = current.next_node
        values += 'NULL\"'
        return values
