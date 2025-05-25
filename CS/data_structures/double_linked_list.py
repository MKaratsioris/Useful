from definitions import DataTypes, Iterables
from node import DoubleNode

"""
TODO    Implement   getters/setters for Node class

TODO    Implement   __add__, iadd__, __le__, etc.
TODO    Implement   insert_after, insert_before, remove_after, remove_before, pop_first, pop_last, first_node, last_node, push_front, push_last

TODO    Implement   is_sorted()

TODO    Implement   sorting algorithm.
TODO    Implement   searching algorithm.

TODO    Implement   logging functionality.
TODO    Implement   unit tests.
"""

class DoubleLinkedList:
    """
    A Double Linked List class representation.
    
    Attributes
    ----------
    head : DoubleNode
        First node of the linked list
    tail: DoubleNode
        Last node of the linked list
    size : int
        Number of nodes in the linked list
    
    Methods
    -------
    length() -> int:
        Returns the total number of nodes the linked list contains.
    print() -> None:
        Prints the linked list using the format '...<---> data <---> data <--->...'
    clear() -> None:
        Removes alls nodes.
    insert(index, data: DataTypes) -> None:
        Inserts the provided data in the specified index. Raises Invalid Insert Index Error.
    insert_data(self, data_reference: DataTypes, new_data: DataTypes) -> None:
        Inserts the new_data after the first occurrence of data_reference. Raises Invalid Insert Data Error.
    insert_list(data_list: list) -> None:
        Insert a collection of data. If data already exists, they are first deleted before proceeding in saving the new data from the list.
    push(self, data: DataTypes) -> None:
        Inserts the provided data in the beginning of the linked list.
    remove(index: int) -> None:
        Removes the data from the specified index. Raises Invalid Delete Index Error.
    remove_data(data: DataTypes) -> None:
        Removes the first node that contains the specified data. Raises Invalid Delete Data Error.
    pop() -> DataTypes:
        Removes the data from the last node.
    """
    def __init__(self) -> None:
        """
        Double Linked List constructor.
        """
        self.head: DoubleNode = None
        self.tail: DoubleNode = None
        self.size: int = 0
    
    def __str__(self) -> str:
        """A reader-friendly string representation of the linked list.

        Returns
        -------
        str
            Data saved in the linked list using the format '...<---> data <---> data <--->...'
        """
        if self.head is None:
            return '[]'
        nodes: list = []
        pointer: DoubleNode = self.head
        while pointer:
            nodes.append(str(pointer.data))
            pointer = pointer.next_node
        return ' <---> '.join(nodes)
    
    def __repr__(self) -> None:
        """A string representation of the linked list.
        
        Returns
        -------
        str
            Data saved in the linked list using the format 'head <--->...<---> data <---> data <--->...<---> None' as well as the total number of nodes it contains.
        """
        return str(self)  + f"\nSize: {self.size} nodes"
    
    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def length(self) -> int:
        """Total number of nodes in the linked list.

        Returns
        -------
        int
            Total number of nodes in the linked list
        """
        return self.size
    
    def print(self, direction: str = 'forward') -> None:
        """Prints the linked list in the specified direction.

        Parameters
        ----------
        direction : str, optional
            Direction to print the linked list, by default 'forward'.
        
        Raises
        ------
        Exception
            Invalid Direction Error
        """
        if not direction in ['forward', 'backward']:
            print("Invalid Direction Error: Please define a valid direction. The direction should take one of the following two values: 'forward' or 'backward'")
            return
        if self.head is None:
            print('[]')
            return
        if direction == 'forward':
            print(self)
            return
        nodes: list = []
        pointer: DoubleNode = self.tail
        while pointer:
            nodes.append(str(pointer.data))
            pointer = pointer.previous_node
        print(' <---> '.join(nodes))
        return
    
    def clear(self) -> None:
        """Removes alls nodes."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self, index: int, data: DataTypes) -> None:
        """Inserts the provided data in the specified index.

        Parameters
        ----------
        index : int
            Index to save the data
        data : DataTypes
            Data to be saved

        Raises
        ------
        Exception
            Invalid Insert Index Error
        """
        if index > self.size or index < 0:
            print(f"Invalid Insert Index Error: The linked list has {self.size} nodes - Index {index} not found.")
            return
        if index == 0:
            new_node: DoubleNode = DoubleNode(data)
            new_node.next_node = self.head
            if self.size == 0:
                self.tail = new_node
            else:
                self.head.previous_node = new_node
            self.head = new_node
            new_node.previous_node = None
            self.size += 1
            print(f"[Add] Data '{data}' added successfully in index {index}.")
            return
        if index == self.size:
            new_node: DoubleNode = DoubleNode(data)
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
            new_node.next_node = None
            self.size += 1
            print(f"[Add] Data '{data}' added successfully in index {index}.")
            return
        count: int = 0
        pointer: DoubleNode = self.head
        while pointer:
            if count == index - 1:
                new_node: DoubleNode = DoubleNode(data=data)
                new_node.next_node = pointer.next_node
                pointer.next_node.previous_node = new_node
                new_node.previous_node = pointer
                pointer.next_node = new_node
                self.size += 1
                print(f"[Add] Data '{data}' added successfully in index {index}.")
                return
            pointer = pointer.next_node
            count += 1
    
    def insert_data(self, data_reference: DataTypes, new_data: DataTypes) -> None:
        """Inserts the new_data after the first occurrence of data_reference.

        Parameters
        ----------
        data_reference : DataTypes
            Data to be positioned before the new_data
        new_data : DataTypes
            Data to be appended after the data_reference

        Raises
        ------
        Exception
            Invalid Insert Data Error
        """
        pointer: DoubleNode = self.head
        if self.head.data == data_reference:
            self.insert(index=1, data=new_data)
            return
        while pointer:
            if pointer.next_node.data == data_reference:
                new_node: DoubleNode = DoubleNode(data=new_data)
                new_node.next_node = pointer.next_node.next_node
                if pointer.next_node != self.tail:
                    pointer.next_node.next_node.previous_node = new_node
                else:
                    self.tail = new_node
                pointer.next_node.next_node = new_node
                new_node.previous_node = pointer.next_node
                self.size += 1
                print(f"[Add] Data '{new_data}' added successfully after data reference '{data_reference}'.")
                return
            pointer = pointer.next_node
            if pointer.next_node is None:
                break
        print(f"Invalid Insert Data Error: Data '{data_reference}' not found.")
        return
    
    def push(self, data: DataTypes) -> None:
        """Inserts the provided data in the beginning of the linked list.

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
        print(f"[Add] Data '{data}' added successfully in index 0.")
        return
    
    def insert_list(self, data_list: Iterables) -> None:
        """Insert a collection of data.

        Parameters
        ----------
        data_list : list | tuple | set
            Iterable collection of data to be saved in the linked list nodes
        """
        self.head = None
        self.tail = None
        self.size = 0
        for data in data_list:
            self.insert(self.size, data)
        self.size = len(data_list)
        print(f"[Add] Data from list were added successfully.")
    
    def remove(self, index: int) -> None:
        """Removes the data from the specified index.

        Parameters
        ----------
        index : int
            Index to remove the data
        
        Raises
        ------
            Invalid Delete Index Error
        """
        if self.size == 0 or index > self.size or index < 0:
            print(f"Invalid Delete Index Error:  The linked list has {self.size} nodes - Index {index} not found.")
            return
        if index == 0:
            data: DataTypes = self.head.data
            self.head = self.head.next_node
            self.head.previous_node = None
            print(f"[Delete] Data '{data}' removed successfully from index {index}.")
            self.size -= 1
            return
        if index == self.size - 1:
            data: DataTypes = self.tail.data
            temp_node: DoubleNode = self.tail.previous_node
            temp_node.next_node = None
            self.tail = temp_node
            print(f"[Delete] Data '{data}' removed successfully from index {index}.")
            self.size -= 1
            return
        if index == self.size:
            print(f"Invalid Delete Index Error:  The linked list has {self.size} nodes - Index {index} not found.")
            return
        count: int = 0
        pointer: DoubleNode = self.head
        while pointer:
            if count > self.size or index >= self.size:
                print(f"Invalid Delete Index Error:  The linked list has {self.size} nodes - Index {index} not found.")
                return
            if count == index - 1:
                data: DataTypes = pointer.next_node.data
                next_node = pointer.next_node.next_node
                next_node.previous_node = pointer
                pointer.next_node = next_node
                print(f"[Delete] Data '{data}' removed successfully from index {index}.")
                self.size -= 1
                return
            pointer = pointer.next_node
            count += 1
    
    def remove_data(self, data: DataTypes) -> None:
        """Removes the first node that contains the specified data.

        Parameters
        ----------
        data : DataTypes
            Data to be removed

        Raises
        ------
        Exception
            Invalid Delete Data Error
        """
        count: int = 0
        pointer: DoubleNode = self.head
        if pointer.data == data:
            self.head = pointer.next_node
            self.head.previous_node = None
            self.size -= 1
            print(f"[Delete] Data '{data}' was removed successfully.")
            return
        while pointer:
            if count <= self.size - 2 and data == pointer.next_node.data:
                next_node = pointer.next_node.next_node
                pointer.next_node = next_node
                if self.tail.data == data:
                    self.tail = pointer
                    self.tail.previous_node = pointer.previous_node
                else:
                    next_node.previous_node = pointer
                self.size -= 1
                print(f"[Delete] Data '{data}' was removed successfully.")
                return
            pointer = pointer.next_node
            count += 1
        print(f"Invalid Delete Data Error: Data {data} not found.")
        return
    
    def pop(self) -> DataTypes:
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
        print(f"[Delete] Data '{data}' was removed successfully from index {self.size}.")
        return data


if __name__ == '__main__':
    double_linked_list: DoubleLinkedList = DoubleLinkedList()
    print(repr(double_linked_list))
    print(len(double_linked_list))
    
    print("\n1. insert")
    double_linked_list.insert(index=0, data=2)
    double_linked_list.insert(index=1, data=5)
    double_linked_list.insert(index=0, data=-1)
    double_linked_list.insert(index=1, data=1)
    double_linked_list.insert(index=double_linked_list.size, data=7)
    double_linked_list.insert(index=double_linked_list.size, data=17)
    double_linked_list.insert(index=double_linked_list.size, data=9)
    double_linked_list.insert(index=double_linked_list.size + 1, data=7)                 # prints InvalidInsertIndexError
    double_linked_list.print()
    double_linked_list.print(direction='forward')
    double_linked_list.print(direction='backward')
    print(double_linked_list)
    print(str(double_linked_list))
    print(repr(double_linked_list))
    
    print("\n2. insert_list")
    double_linked_list.insert_list(data_list=[0, 1, 2, 3, 4, 5, 6])
    print(repr(double_linked_list))
    double_linked_list.print(direction='backward')
    
    print("\n3. clear")
    double_linked_list.clear()
    print(repr(double_linked_list))
    double_linked_list.print(direction='backward')
    
    print("\n4. insert_data")
    double_linked_list.insert_list(data_list=[-2, 0, 2, 3, 4, 5, 6, 7])
    double_linked_list.insert_data(data_reference=-2, new_data=-1)
    double_linked_list.insert_data(data_reference=7, new_data=8)
    double_linked_list.insert_data(data_reference=0, new_data=1)
    print(repr(double_linked_list))
    double_linked_list.insert_data(data_reference=10, new_data=7)                 # prints InvalidInsertDataError
    double_linked_list.print(direction='backward')
    
    print("\n5. remove")
    double_linked_list.remove(index=0)
    print(repr(double_linked_list))
    double_linked_list.remove(index=3)
    print(repr(double_linked_list))
    double_linked_list.remove(index=8)
    print(repr(double_linked_list))
    double_linked_list.remove(index=double_linked_list.size)                             # prints InvalidDeleteIndexError
    double_linked_list.print(direction='backward')
    
    print("\n6. remove_data")
    double_linked_list.remove_data(data=-1)
    print(repr(double_linked_list))
    double_linked_list.remove_data(data=3)
    print(repr(double_linked_list))
    double_linked_list.remove_data(data=7)
    print(repr(double_linked_list))
    double_linked_list.remove_data(data=10)                                        # prints InvalidDeleteIndexError
    double_linked_list.print(direction='backward')

    print("\n7. pop")
    data_popped = double_linked_list.pop()
    print(f"{data_popped=}")
    print(repr(double_linked_list))
    double_linked_list.print(direction='backward')
    data_popped = double_linked_list.pop()
    print(f"{data_popped=}")
    print(repr(double_linked_list))
    data_popped = double_linked_list.pop()
    print(f"{data_popped=}")
    print(repr(double_linked_list))
    double_linked_list.print(direction='backward')
    
    print("\n8. push")
    data_popped = double_linked_list.push(data=-10)
    data_popped = double_linked_list.push(data=-20)
    data_popped = double_linked_list.push(data=-30)
    print(repr(double_linked_list))
    double_linked_list.print(direction='backward')
    