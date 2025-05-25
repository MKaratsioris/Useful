from definitions import DataTypes, Iterables
from node import DoubleNode

"""
TODO    Implement   self.limit: When queue if full, then when an item is added, the last item is discarded automatically.

TODO    Implement   __add__, iadd__, __le__, etc.

TODO    Implement   searching algorithm.

TODO    Implement   logging functionality.
TODO    Implement   unit tests.

?TODO   Implement   a Parent class or Interface for Stack, Linked List and Queue
"""

class Queue:
    """
    A Queue class representation following the FIFO principle.
    
    Attributes
    ----------
    head : DoubleNode
        First node of the queue
    tail: DoubleNode
        Last node of the queue
    size : int
        Number of nodes in the queue
    
    Methods
    -------
    length() -> int:
        Returns the total number of nodes the queue contains.
    print() -> None:
        Prints the queue using the format '...<---> data <---> data <--->...'
    clear() -> None:
        Removes alls nodes.
    enqueue(data: DataTypes) -> None:
        Inserts the provided data in the back of the queue.
    enqueue(data_list: Iterables) -> None:
        Insert a collection of data in the back of the queue.
    dequeue() -> DataTypes:
        Removes the data from the front of the queue and returns the data.
    peek() -> DataTypes
        Returns the data in the front of queue without removing it.
    """
    def __init__(self) -> None:
        """Queue constructor."""
        self.head: DoubleNode = None
        self.tail: DoubleNode = None
        self.size: int = 0
        self.limit: int = None
    
    def __str__(self) -> str:
        """A reader-friendly string representation of the queue.

        Returns
        -------
        str
            Data saved in the queue using the format '...---> data ---> data --->...'
        """
        if self.head is None:
            return '[]'
        nodes: list = []
        pointer: DoubleNode = self.head
        while pointer:
            nodes.append(str(pointer.data))
            pointer = pointer.next_node
        return ' ---> '.join(nodes)
    
    def __repr__(self) -> None:
        """A string representation of the queue.
        
        Returns
        -------
        str
            Data saved in the queue using the format '...---> data ---> data' as well as the total number of nodes it contains.
        """
        return str(self)  + f"\nSize: {self.size} nodes"
    
    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def length(self) -> int:
        """Total number of nodes in the queue.

        Returns
        -------
        int
            Total number of nodes in the queue
        """
        return self.size
    
    def print(self) -> None:
        """Prints the queue in the specified direction."""
        if self.head is None:
            print('[]')
            return
        print(self)
        return
    
    def clear(self) -> None:
        """Removes alls nodes."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, data: DataTypes) -> None:
        """Inserts the provided data in the back of the queue.

        Parameters
        ----------
        data : DataTypes
            Data to be saved
        """
        new_node: DoubleNode = DoubleNode(data)
        new_node.next_node = self.head
        if self.size == 0:
            self.tail = new_node
        else:
            self.head.previous_node = new_node
        self.head = new_node
        new_node.previous_node = None
        self.size += 1
        print(f"[Add] Data '{data}' added successfully.")
        return
    
    def enqueue_list(self, data_list: Iterables) -> None:
        """Insert a collection of data in the back of the queue.

        Parameters
        ----------
        data_list : list | tuple | set
            Iterable collection of data to be saved in the queue nodes
        """
        self.head = None
        self.tail = None
        self.size = 0
        for data in data_list:
            self.enqueue(data=data)
        self.size = len(data_list)
        print(f"[Add] Data from list were added successfully.")
    
    def dequeue(self) -> DataTypes:
        """
        Removes the data from the last node and returns it.
        
        Returns
        -------
        DataTypes
            Data that were saved in the last node.
        """
        data: DataTypes = self.tail.data
        self.tail = self.tail.previous_node
        self.tail.next_node = None
        self.size -= 1
        print(f"[Delete] Data '{data}' was removed successfully.")
        return data
    
    def peek(self) -> DataTypes:
        """
        Returns the data in the front of queue without removing it.
        
        Returns
        -------
        DataTypes
            Data that were saved in the last node.
        """
        return self.tail.data
        


if __name__ == '__main__':
    queue: Queue = Queue()
    print(repr(queue))
    print(len(queue))
    
    print("\n1. enqueue_list")
    queue.enqueue_list(data_list=[0, 1, 2, 3, 4, 5, 6][::-1])
    print(repr(queue))
    
    print("\n2. clear")
    queue.clear()
    print(repr(queue))

    print("\n3. dequeue")
    queue.enqueue_list(data_list=[0, 1, 2, 3, 4, 5, 6][::-1])
    print(repr(queue))
    data_popped = queue.dequeue()
    print(f"{data_popped=}")
    print(repr(queue))
    data_popped = queue.dequeue()
    print(f"{data_popped=}")
    print(repr(queue))
    data_popped = queue.dequeue()
    print(f"{data_popped=}")
    print(repr(queue))
    
    print("\n4. enqueue")
    data_popped = queue.enqueue(data=-10)
    data_popped = queue.enqueue(data=-20)
    data_popped = queue.enqueue(data=-30)
    print(repr(queue))
    