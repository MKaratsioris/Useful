from timeit import timeit
from typing import Iterator
import this # prints in the terminal the Zen of Python

class SlotsProfile:
    __slots__ = ("name", "age", "items") # It overrides the __dict__ which can save quite some memory
    
    def __init__(self, name:str, age:int, *items: str):
        self.name: str = name
        self.age: int = age
        self.items = list(items)
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nAge: {self.age}"
    
    def __add__(self, item: str):
        self.items.append(item)
        return self
    
    def __sub__(self, item: str):
        self.items.remove(item)
        return self
    
    def __contains__(self, item: str) -> bool:
        return item in self.items
    
    def __iter__(self) -> Iterator[str]:
        return iter(self.items)

class NoSlotsProfile:
    
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age


if __name__ == "__main__":
    print("\n\n-------- __slots__ --------\n\n")
    print("\t\t\t--- WITH SLOTS ---\n")
    profile_slots = SlotsProfile("Julian", 33)
    print(f"\t\t\tNAME: {profile_slots.name}")
    print(f"\t\t\tAGE: {profile_slots.age}")
    print(f"\t\t\tSIZE: {profile_slots.__slots__.__sizeof__()} bytes") # 88 bytes
    setup = """
class SlotsProfile:
    __slots__ = ("name", "age") # It overrides the __dict__ which can save quite some memory
    
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    """
    code = """profile_slots = SlotsProfile("Julian", 33)"""
    time_slots = timeit(code, setup=setup, number=1_000_000)
    print(f"\t\t\tTime to create 1,000,000 instances with slots: {time_slots} seconds.") # 0.0983056710101664"
    
    print("\n\t\t\t--- WITHOUT SLOTS ---\n")
    profile_no_slots = NoSlotsProfile("Julian", 33)
    print(f"\t\t\tNAME: {profile_no_slots.name}")
    print(f"\t\t\tAGE: {profile_no_slots.age}")
    print(f"\t\t\tdictionary: {profile_no_slots.__dict__}") # Works when there is no __slots__
    print(f"\t\t\tSIZE: {profile_no_slots.__dict__.__sizeof__()} bytes") # 88 bytes
    setup = """
class NoSlotsProfile:
    
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    """
    code = """profile_no_slots = NoSlotsProfile("Julian", 33)"""
    time_no_slots = timeit(code, setup=setup, number=1_000_000)
    print(f"\t\t\tTime to create 1,000,000 instances with no slots: {time_no_slots} seconds.") # 0.12826303101610392"
    #The following line will produce an error for the __slots__ case
    profile_no_slots.gender = "M"
    print(f"\t\t\tGENDER: {profile_no_slots.gender}")
    print(f"\t\t\tnew dictionary: {profile_no_slots.__dict__}") # Works when there is no __slots__
    print(f"\t\t\tnew SIZE: {profile_no_slots.__dict__.__sizeof__()} bytes")
    
    print(f"\n\n\t\t\tTime difference: {((time_no_slots - time_slots) / time_no_slots) * 100:.2f}%") # 23.36%
    
    print("\n\n-------- __str__ --------\n")
    print(profile_slots)
    
    print("\n\n-------- __add__ --------\n")
    profile_slots = profile_slots + "first item"
    profile_slots += "second item"
    profile_slots += "third item"
    profile_slots += "fourth item"
    print(profile_slots.items)
    
    print("\n\n-------- __sub__ --------\n")
    profile_slots = profile_slots - "fourth item"
    profile_slots = profile_slots - "third item"
    print(profile_slots.items)
    
    print("\n\n-------- __contains__ --------\n")
    contains_first_item = "first item" in profile_slots.items
    contains_second_item = "second item" in profile_slots.items
    contains_third_item = "third item" in profile_slots.items
    contains_fourth_item = "fourth item" in profile_slots.items
    print(f"\t\t\tContains 'first item': {contains_first_item}")
    print(f"\t\t\tContains 'second item': {contains_second_item}")
    print(f"\t\t\tContains 'third item': {contains_third_item}")
    print(f"\t\t\tContains 'fourth item': {contains_fourth_item}")
    
    print("\n\n-------- __iter__ --------\n")
    for i, item in enumerate(profile_slots):
        print(f"{i + 1}. {item}")