from node import SingleNode
from definitions import Iterables, DataTypes

"""
TODO    Implement   self.limit: When a stack is full, there should not be possible to add items.

TODO    Implement   __add__, iadd__, __le__, etc.

TODO    Implement   searching algorithm.

TODO    Implement   logging functionality.
TODO    Implement   unit tests.

?TODO   Implement   a Parent class for Stack, Linked List and Queue
"""

class Stack:
    """
    A Stack class representation following the LIFO principle.
    
    Attributes
    ----------
    head : SingleNode
        First node of the stack
    size : int=None
        Number of nodes in the stack
    
    Methods
    -------
    length() -> int:
        Returns the total number of nodes the stack contains.
    print() -> None:
        Prints the stack using the format '...---> data ---> data --->...'
    clear() -> None:
        Removes alls nodes.
    insert_list(data_list: list) -> None:
        Insert a collection of data. If data already exists, they are first deleted before proceeding in saving the new data from the list.
    push(self, data: DataTypes) -> None:
        Inserts the provided data in the beginning of the stack.
    pop() -> DataTypes:
        Removes the data from the beginning of the stack.
    """
    def __init__(self) -> None:
        """
        Single stack constructor.
        """
        self.head: SingleNode = None
        self.size: int = 0
        self.limit: int = None
    
    def __str__(self) -> str:
        """A reader-friendly string representation of the stack.

        Returns
        -------
        str
            Data saved in the stack using the format '...---> data ---> data --->...'
        """
        if self.head is None:
            return '[]'
        nodes: list = []
        pointer: SingleNode = self.head
        while pointer:
            nodes.append(str(pointer.data))
            pointer = pointer.next_node
        return ' ---> '.join(nodes)
    
    def __repr__(self) -> str:
        """A string representation of the stack.
        
        Returns
        -------
        str
            Data saved in the stack using the format '...---> data ---> data --->...' as well as the total number of nodes it contains.
        """
        return str(self)  + f"\nSize: {self.size} nodes"
    
    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def length(self) -> int:
        """Total number of nodes in the stack.

        Returns
        -------
        int
            Total number of nodes in the stack
        """
        return self.size
    
    def print(self) -> None:
        print(self)
    
    def clear(self) -> None:
        """Removes alls nodes."""
        self.head = None
        self.size = 0
    
    def insert_list(self, data_iterable: Iterables) -> None:
        """Insert a collection of data.

        Parameters
        ----------
        data_list : list | tuple | set | frozenset | bytearray
            Iterable collection of data to be saved in the stack nodes
        """
        self.head = None
        self.size = 0
        for data in data_iterable:
            self.push(data=data)
        self.size = len(data_iterable)
        print(f"[Add] Data from list were added successfully.")
    
    def push(self, data: DataTypes) -> None:
        """Inserts the provided data in the beginning of the stack.

        Parameters
        ----------
        data : DataTypes
            Data to be saved
        """
        self.head = SingleNode(data=data, next_node=self.head)
        self.size += 1
        print(f"[Add] Data '{data}' added successfully.")
        return
    
    def pop(self, number_items: int = 1) -> DataTypes:
        """
        Removes the data from the beginning of the stack and returns it.
        
        Returns
        -------
        DataTypes
            Data that were saved in the first node.
        """
        if number_items > 1:
            data: list[DataTypes] = []
            for _ in range(number_items):
                data.append(self.head.data)
                print(f"[Delete] Data '{self.head.data}' was removed successfully.")
                self.head = self.head.next_node
                self.size -= 1
                if self.size == 0:
                    break
        else:
            data: DataTypes = self.head.data
            self.head = self.head.next_node
            self.size -= 1
            print(f"[Delete] Data '{data}' was removed successfully.")
        return data


if __name__ == '__main__':
    stack: Stack = Stack()
    print(repr(stack))
    print(len(stack))
    
    print("\n1. insert_list")
    stack.insert_list(data_iterable=[0, 1, 2, 3, 4, 5, 6][::-1])
    stack.print()
    print(repr(stack))
    
    print("\n2. clear")
    stack.clear()
    print(repr(stack))
    
    print("\n3. pop")
    stack.insert_list(data_iterable=[0, 1, 2, 3, 4, 5, 6][::-1])
    data_popped = stack.pop()
    print(f"{data_popped=}")
    data_popped = stack.pop()
    print(f"{data_popped=}")
    data_popped = stack.pop()
    print(f"{data_popped=}")
    print(repr(stack))
    data_popped = stack.pop(number_items=2)
    print(f"{data_popped=}")
    print(repr(stack))
    data_popped = stack.pop(number_items=30)
    print(f"{data_popped=}")
    print(repr(stack))
    
    print("\n4. push")
    data_popped = stack.push(data=-10)
    data_popped = stack.push(data=-20)
    data_popped = stack.push(data=-30)
    print(repr(stack))
    data_popped = stack.pop(number_items=1)
    print(f"{data_popped=}")
    print(repr(stack))

