from __future__ import annotations
from typing import Optional
from collections import deque

from definitions import DataTypes

"""
TODO    Implement   getters/setters for Node class

TODO    Implement   logging functionality.
TODO    Implement   unit tests.
"""

""" Iterables = list | tuple | set | frozenset | bytearray
Simple = int | float | complex | str | bool | bytes | memoryview
DataTypes = Simple | Iterables | dict """

class SingleNode:
    """
    A Node class representation, used in Single Linked List.
    
    Attributes
    ----------
    data : DataTypes
        Data to be saved in the node
    next_node : SingleNode
        The next node
    """
    def __init__(self, data: DataTypes, next_node: Optional[SingleNode] = None) -> None: # type: ignore
        self.data: DataTypes = data # type: ignore
        self.next_node: SingleNode = next_node
    
    def __str__(self) -> str:
        return f"SingleNode(data={self.data}, next_node={self.next_node})"
    
    def __repr__(self) -> str:
        return f"SingleNode(data={self.data}, next_node={self.next_node})"

class DoubleNode:
    """
    A Node class representation, used in Double Linked List.
    
    Attributes
    ----------
    data : DataTypes
        Data to be saved in the node
    previous_node : DoubleNode
        The previous node
    next_node : DoubleNode
        The next node
    """
    def __init__(self, data: DataTypes, previous_node: Optional[DoubleNode] = None, next_node: Optional[DoubleNode] = None) -> None: # type: ignore
        self.data: DataTypes = data # type: ignore
        self.previous_node: DoubleNode = previous_node
        self.next_node: DoubleNode = next_node
    
    def __str__(self) -> str:
        return f"DoubleNode(data={self.data})"
    
    def __repr__(self) -> str:
        return f"DoubleNode(data={self.data})"

class TreeNode:
    """
    A Node class representation, used in Tree.
    
    Attributes
    ----------
    data : DataTypes
        Data to be saved in the node
    children : list[TreeNode]
        A list with all the nodes with one level down
    parent : TreeNode
        The node with one level up
    level : int
        Level of the node in the Tree
    
    Methods
    -------
    add_child(self, child: TreeNode) -> None

    show(self, depth: int = None) -> None

    depth_first_search(self, node: TreeNode = None) -> None

    breadth_first_search(self, node: TreeNode = None) -> None

    it_has(self, data, node: TreeNode = None) -> bool

    """
    def __init__(self, data: DataTypes) -> None:
        self.data: DataTypes = data
        self.children: list[TreeNode] = []
        self.parent: TreeNode = None
        self.level: int = 0
    
    def add_child(self, child: TreeNode) -> None:
        """_summary_

        Parameters
        ----------
        child : TreeNode
            _description_
        """
        child.parent = self
        self.children.append(child)
        child.level = self.level + 1
    
    def show(self, depth: int = None) -> None:
        """_summary_

        Parameters
        ----------
        depth : int, optional
            _description_, by default None
        """
        if depth is None:
            depth = self.level
        elif self.level > depth:
            return
        spaces: str = ' ' * self.level * 3
        prefix: str = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.show(depth=depth)
    
    def depth_first_search(self, node: TreeNode = None) -> None:
        """_summary_

        Parameters
        ----------
        node : TreeNode, optional
            _description_, by default None
        """
        if node is None:
            node = self
        print(node.data)
        for child in node.children:
            self.depth_first_search(node=child)
    
    def breadth_first_search(self, node: TreeNode = None) -> None:
        """_summary_

        Parameters
        ----------
        node : TreeNode, optional
            _description_, by default None
        """
        if node is None:
            node = self
        queue: deque = deque([node])
        
        while queue:
            current_node: TreeNode = queue.popleft()
            print(current_node.data)
            queue.extend(current_node.children)
    
    def it_has(self, data, node: TreeNode = None) -> bool:
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        node : TreeNode, optional
            _description_, by default None

        Returns
        -------
        bool
            _description_
        """
        if node is None:
            node = self
        if node.data == data:
            return True
        for child in node.children:
            result = self.it_has(data=data, node=child)
            if result:
                return result
        return False

if __name__ == '__main__':
    print("\n=========== SINGLE NODE ===========\n")
    print("Saving integer in the node.")
    first_node: SingleNode = SingleNode(data=1)
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    second_node: SingleNode = SingleNode(data=2)
    third_node: SingleNode = SingleNode(data=4)
    
    
    first_node.next_node = second_node
    second_node.next_node = third_node
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    new_node = SingleNode(data=3)
    new_node.next_node = third_node
    second_node.next_node = new_node
    print(f"\n{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{new_node.data=}")
    print(f"{new_node.next_node=}")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    
    
    print("\nSaving string in the node.")
    first_node: SingleNode = SingleNode(data="1")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    second_node: SingleNode = SingleNode(data="2")
    third_node: SingleNode = SingleNode(data="4")
    
    
    first_node.next_node = second_node
    second_node.next_node = third_node
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    
    
    print("\n=========== DOUBLE NODE ===========\n")
    print("Saving integer in the node.")
    first_node: DoubleNode = DoubleNode(data=1)
    second_node: DoubleNode = DoubleNode(data=2)
    third_node: DoubleNode = DoubleNode(data=4)
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    print("\n---------------------")
    first_node.next_node = second_node
    second_node.previous_node = first_node
    second_node.next_node = third_node
    third_node.previous_node = second_node
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    new_node = DoubleNode(data=3)
    new_node.next_node = third_node
    new_node.previous_node = second_node
    second_node.next_node = new_node
    third_node.previous_node = new_node
    print("\n---------------------")
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{new_node.data=}")
    print(f"{new_node.next_node=}")
    print(f"{new_node.previous_node=}")
    print("\nFourth Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    
    
    print("\nSaving string in the node.")
    first_node: DoubleNode = DoubleNode(data="1")
    second_node: DoubleNode = DoubleNode(data="2")
    third_node: DoubleNode = DoubleNode(data="4")
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    print("\n---------------------")
    first_node.next_node = second_node
    second_node.previous_node = first_node
    second_node.next_node = third_node
    third_node.previous_node = second_node
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    
    
    print("\n=========== TREE NODE ===========")
    print("\n1. add_child")
    root = TreeNode(data='Electronics')
    laptop = TreeNode(data='Laptop')
    cellphone = TreeNode(data='Cellphone')
    tv = TreeNode(data='TV')
    root.add_child(child=laptop)
    root.add_child(child=cellphone)
    root.add_child(child=tv)
    print(f"{len(root.children)=}")
    print(f"{root.data=}")
    print(f"{root.children[0].parent.data=}")
    print(f"{root.children[0].data=}")
    print(f"{len(root.children[0].children)=}")
    
    print("\n2. show")
    laptop.add_child(child=TreeNode(data='Macbook Pro'))
    laptop.add_child(child=TreeNode(data='Surface'))
    laptop.add_child(child=TreeNode(data='Thinkpad'))
    cellphone.add_child(child=TreeNode(data='iPhone'))
    cellphone.add_child(child=TreeNode(data='Google Pixel'))
    cellphone.add_child(child=TreeNode(data='Vivo'))
    tv.add_child(child=TreeNode(data='LG'))
    tv.add_child(child=TreeNode(data='Samsung'))
    for level in range(3):
        print(f"\n----- {level=} -----")
        root.show(depth=level)
    root.depth_first_search()
    root.breadth_first_search()
    print(f"{root.it_has(data='LG')=}")
    print(f"{root.it_has(data='LGI')=}")