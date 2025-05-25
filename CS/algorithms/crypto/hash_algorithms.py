
#ITERABLE_TYPES = TypeVar(list, tuple, dict, set, frozenset, bytearray)
#Iterables = list | tuple | dict | set | frozenset | bytearray
#Simple = int | float | complex | str
#DATA_TYPES = TypeVar(int, float, complex, str, bool, bytes, memoryview, ITERABLE_TYPES)
#DataTypes = Simple | Iterables | bool | bytes | memoryview
DataOrder = str | bytes | bytearray

def hash_unicode(self, key: DataOrder) -> int:
    total: int = None
    for character in str(key):
        total += ord(character)
    return total % self.MAX