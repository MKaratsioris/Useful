from __future__ import annotations

"""
TODO    Change      self.items_list, self.values and self.keys from list[list] to list[SingleLinkedList] for optimal append time and memory management.

TODO    Implement   __add__, iadd__, etc.

TODO    Implement   logging functionality.
TODO    Implement   unit tests.


Load factor = (Number of items in the hash table) / (Total number of slots)

Having a load factor greater than 1 means you have more items than slots in your array.
Once the load factor starts to grow, you need to add more slots to your hash table. his is called resizing.
A good rule of thumb is, resize when your load factor is greater than 0.7.

A good hash function is the SHA function.

"""

#ITERABLE_TYPES = TypeVar(list, tuple, dict, set, frozenset, bytearray)
Iterables = list | tuple | dict | set | frozenset | bytearray
Simple = int | float | str
#DATA_TYPES = TypeVar(int, float, complex, str, bool, bytes, memoryview, ITERABLE_TYPES)
DataTypes = Simple | Iterables | bool | bytes | memoryview | complex


class HashTable:
    """
    
    """
    def __init__(self, hashing: str = "chaining") -> None:
        self.MAX: int = 10
        self.keys: list[Simple] = []
        self.items_list: list[list[Simple]] = [[] for _ in range(self.MAX)]
        self.values: list[Simple] = []
        self.hashing: str = hashing
        self.capacity: float = 0.0
    
    def __setitem__(self, key: Simple, value: DataTypes) -> None:
        self.__check_capacity()
        self.keys.append(key)
        self.values.append(value)
        index: int = self.hash(key=key)
        if self.hashing == "chaining":
            print(f"--------> Chaining Method")
            print(f"Index: {index}")
            """
            Collision Handling method: Linear Probing
            
            Storing key-value pairs as tuples in the list that is saved in the index of the list 'items_list'.
            If a collision takes place, then the new tuple is appended in the list.
            """
            for key_value in self.items_list[index]:
                if len(key_value) == 2 and key_value[0] == key:
                    key_value = (key, value)
                    return
            self.items_list[index].append((key, value))
            return
        if self.hashing == "linear_probing":
            print(f"--------> Linear Probing Method")
            """
            Collision Handling method: Linear Probing
            
            Storing key-value pairs as tuples in the list 'items_list' in the hashed index.
            If a collision takes place, then the new tuple is appended in the list in the next available index.
            """
            return
        #print(f"Invalid Key-Value Error: Could not save the following key-value: {{{key}: {value}}}.")
    
    def __getitem__(self, key: Simple) -> DataTypes:
        index: int = self.hash(key=key)
        for key_value in self.items_list[index]:
            if key_value[0] == key:
                return key_value[1]
        return ""
    
    def __delitem__(self, key: Simple) -> None:
        index: int = self.hash(key=key)
        for i, key_value in enumerate(self.items_list[index]):
            if key_value[0] == key:
                del self.items_list[index][i]
                return
    
    def __str__(self) -> str:
        """A reader-friendly string representation of the HashTable, one key-value pair per line.

        Returns
        -------
        str
            Data saved in the HashTable using the format
            {
                key: value,
            }
        """
        if self.is_empty():
            return "{}"
        string_representation: str = "{\n"
        for index, key_value in enumerate(self.items_list):
            if len(self.items_list[index]) == 1:
                string_representation += f"\t{key_value[0][0]}: {key_value[0][1]},\n"
            elif len(self.items_list[index]) >= 2:
                for data_point in self.items_list[index]:
                    string_representation += f"\t{data_point[0]}: {data_point[1]},\n"
        string_representation += "}"
        return string_representation
    
    def __repr__(self) -> str:
        """A reader-friendly string representation of the HashTable, in a compact form.

        Returns
        -------
        str
            Data saved in the HashTable using the format
            { key: value, ...}
        """
        if self.is_empty():
            return "{}"
        string_representation: str = "{"
        for index, key_value in enumerate(self.items_list):
            if len(self.items_list[index]) == 1:
                string_representation += f" {key_value[0][0]}: {key_value[0][1]},"
            elif len(self.items_list[index]) >= 2:
                for data_point in self.items_list[index]:
                    string_representation += f" {data_point[0]}: {data_point[1]},"
        string_representation = string_representation[:-1] + " }"
        return string_representation
    
    def print(self) -> None:
        print(str(self))
    
    def is_empty(self) -> bool:
        return len(self.keys) == 0 and len(self.values) == 0
    
    def capacity(self) -> float:
        return self.capacity
    
    def __check_capacity(self) -> None:
        if self.capacity >= 0.7:
            self.items_list += [[] for _ in range(self.MAX)]
            self.MAX *= 2
            self.capacity = len(self.items_list) / self.MAX
            print("--------> Doubled the size of items_list!!!!!!!!!")
    
    def hash(self, key: Simple) -> int:
        total: int = 0
        for character in str(key):
            total += ord(character)
        return total % self.MAX
    
    def keys(self) -> list[Simple]:
        return self.keys
    
    def values(self) -> list[Simple]:
        return self.values
        
    def items(self) -> list[tuple[Simple, Simple]]:
        result: list[tuple[Simple, Simple]] = []
        for key_value_list in self.items_list:
            if len(key_value_list) == 1:
                result.append(key_value_list[0])
            if len(key_value_list) >= 1:
                for key_value in key_value_list:
                    result.append(key_value)
        return result



if __name__ == '__main__':
    hash_table: HashTable = HashTable()
    hash_table.print()
    print(repr(hash_table))
    index: int = hash_table.hash('Michalis')
    print(f"Index for 'Michalis' => {index}")
    hash_table['Michalis'] = 40
    print(f"{hash_table.items_list[index]=}")
    print(f"{hash_table.keys=}")
    print(f"{hash_table.items_list=}")
    print(f"{hash_table['Michalis']=}")
    hash_table.print()
    print(repr(hash_table))
    hash_table['Alejandra'] = 10
    hash_table['Harris'] = 20
    hash_table['Tina'] = 30
    hash_table['Vickyyy'] = 31
    print(f"{hash_table.items_list=}")
    hash_table.print()
    print(repr(hash_table))
    del hash_table['Tina']
    print(f"{hash_table.items_list=}")
    print(f"{hash_table['Michalis']=}")
    print(f"{hash_table['Alejandra']=}")
    print(f"{hash_table['Harris']=}")
    print(f"{hash_table['Vickyyy']=}")
    hash_table.print()
    print(f"{hash_table['Tina']=}")
    print(f"{hash_table['Sarantis']=}")
    del hash_table['Vickyyy']
    print(f"{hash_table.items_list=}")
    del hash_table['Sarantis']
    print(f"{hash_table['Sarantis']=}")
    hash_table.print()
    print(repr(hash_table))
    