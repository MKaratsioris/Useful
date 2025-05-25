from node import SingleNode
from definitions import DataTypes, Iterables

"""
TODO    Implement   __add__, iadd__, __le__, etc.
TODO    Implement   insert_after, insert_before, remove_after, remove_before, pop_first, pop_last, first_node, last_node, push_front, push_last

TODO    Implement   is_sorted()

TODO    Implement   sorting algorithm.
TODO    Implement   searching algorithm.

TODO    Implement   logging functionality.
TODO    Implement   unit tests.

?TODO   Implement   a Parent class for Stack, Linked List and Queue
"""

class SingleLinkedList:
    """
    A Single Linked List class representation.
    
    Attributes
    ----------
    head : SingleNode
        First node of the linked list
    size : int=None
        Number of nodes in the linked list
    
    Methods
    -------
    length() -> int:
        Returns the total number of nodes the linked list contains.
    print() -> None:
        Prints the linked list using the format 'head --->...---> data ---> data --->...---> None'
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
        """Single Linked List constructor."""
        self.head: SingleNode = None
        self.size: int = 0
    
    def __str__(self) -> str:
        """A reader-friendly string representation of the linked list.

        Returns
        -------
        str
            Data saved in the linked list using the format '...---> data ---> data --->...'
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
        """A string representation of the linked list.
        
        Returns
        -------
        str
            Data saved in the linked list using the format '...---> data ---> data --->...' as well as the total number of nodes it contains.
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
    
    def print(self) -> None:
        print(self)
    
    def clear(self) -> None:
        """Removes alls nodes."""
        self.head = None
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
            self.head = SingleNode(data, self.head)
            self.size += 1
            print(f"[Add] Data '{data}' added successfully in index {index}.")
            return
        if index == self.size:
            pointer: SingleNode = self.head
            while pointer.next_node:
                pointer = pointer.next_node
            pointer.next_node = SingleNode(data, None)
            self.size += 1
            print(f"[Add] Data '{data}' added successfully in index {index}.")
            return
        count: int = 0
        pointer: SingleNode = self.head
        while pointer:
            if count == index - 1:
                temp_node: SingleNode = SingleNode(data, pointer.next_node)
                pointer.next_node = temp_node
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
        pointer: SingleNode = self.head
        while pointer:
            if pointer.data == data_reference:
                temp_node: SingleNode = SingleNode(new_data, pointer.next_node)
                pointer.next_node = temp_node
                self.size += 1
                print(f"[Add] New data '{new_data}' was added successfully after data reference '{data_reference}'.")
                return
            pointer = pointer.next_node
        print(f"Invalid Insert Data Error: Data '{data_reference}' not found.")
        return
    
    def insert_list(self, data_iterable: Iterables) -> None:
        """Insert a collection of data.

        Parameters
        ----------
        data_iterable : 
            Iterable collection of data to be saved in the linked list nodes
        """
        self.head = None
        self.size = 0
        for data in data_iterable:
            self.insert(self.size, data)
        self.size = len(data_iterable)
        print(f"[Add] Data from list were added successfully.")
    
    def push(self, data: DataTypes) -> None:
        """Inserts the provided data in the beginning of the linked list.

        Parameters
        ----------
        data : DataTypes
            Data to be saved
        """
        self.head = SingleNode(data=data, next_node=self.head)
        self.size += 1
        print(f"[Add] Data '{data}' added successfully in index 0.")
        return
    
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
            self.size -= 1
            print(f"[Delete] Data '{data}' was removed successfully from index {index}.")
            return            
        count: int = 0
        pointer: SingleNode = self.head
        while pointer:
            if count > self.size or index >= self.size:
                print(f"Invalid Delete Index Error:  The linked list has {self.size} nodes - Index {index} not found.")
                return
            if count == index - 1:
                data: DataTypes = pointer.next_node.data
                pointer.next_node = pointer.next_node.next_node
                self.size -= 1
                print(f"[Delete] Data '{data}' was removed successfully from index {index}.")
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
        pointer: SingleNode = self.head
        if pointer.data == data:
            self.head = pointer.next_node
            self.size -= 1
            print(f"[Delete] Data '{data}' was removed successfully.")
            return
        while pointer:
            if count <= self.size - 2 and data == pointer.next_node.data:
                pointer.next_node = pointer.next_node.next_node
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
        count: int = 0
        data: DataTypes = None
        pointer: SingleNode = self.head
        while count <= self.size - 3:
            pointer = pointer.next_node
            count += 1
        data: DataTypes = pointer.next_node.data
        pointer.next_node = None
        self.size -= 1
        return data


if __name__ == '__main__':
    single_linked_list: SingleLinkedList = SingleLinkedList()
    print(repr(single_linked_list))
    print(len(single_linked_list))
    
    print("\n1. insert")
    single_linked_list.insert(index=0, data=2)
    single_linked_list.insert(index=1, data=5)
    single_linked_list.insert(index=single_linked_list.size, data=7)
    single_linked_list.insert(index=single_linked_list.size, data=17)
    single_linked_list.insert(index=single_linked_list.size, data=9)
    single_linked_list.insert(index=single_linked_list.size + 1, data=7)    # prints InvalidInsertIndexError
    single_linked_list.insert(index=1, data=5)
    single_linked_list.print()
    print(single_linked_list)
    print(str(single_linked_list))
    print(repr(single_linked_list))
    
    print("\n2. insert_list")
    single_linked_list.insert_list(data_iterable=[0, 1, 2, 3, 4, 5, 6])
    single_linked_list.print()
    print(repr(single_linked_list))
    
    print("\n3. clear")
    single_linked_list.clear()
    print(repr(single_linked_list))
    
    print("\n4. insert_data")
    single_linked_list.insert_list(data_iterable=[-2, 0, 2, 3, 4, 5, 6, 7])
    print(repr(single_linked_list))
    single_linked_list.insert_data(data_reference=-2, new_data=-1)
    single_linked_list.insert_data(data_reference=7, new_data=8)
    single_linked_list.insert_data(data_reference=0, new_data=1)
    print(repr(single_linked_list))
    single_linked_list.insert_data(data_reference=10, new_data=7)   # prints InvalidInsertDataError
    
    print("\n5. remove")
    single_linked_list.remove(index=0)
    single_linked_list.remove(index=3)
    single_linked_list.remove(index=single_linked_list.size - 1)
    single_linked_list.remove(index=single_linked_list.size)    # prints InvalidDeleteIndexError
    print(repr(single_linked_list))
    
    print("\n6. remove_data")
    single_linked_list.remove_data(data=-1)
    single_linked_list.remove_data(data=3)
    single_linked_list.remove_data(data=7)
    single_linked_list.remove_data(data=10) # prints InvalidDeleteIndexError
    print(repr(single_linked_list))
    
    print("\n7. pop")
    data_popped = single_linked_list.pop()
    print(f"{data_popped=}")
    data_popped = single_linked_list.pop()
    print(f"{data_popped=}")
    data_popped = single_linked_list.pop()
    print(f"{data_popped=}")
    print(repr(single_linked_list))
    
    print("\n8. push")
    data_popped = single_linked_list.push(data=-10)
    data_popped = single_linked_list.push(data=-20)
    data_popped = single_linked_list.push(data=-30)
    print(repr(single_linked_list))