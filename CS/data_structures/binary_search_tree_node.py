from typing import Any
from collections.abc import Iterable
from random import randint

class BinarySearchTreeNode:
    """
    TODO    Implement pre_order_traversal
    TODO    Implement post_order_traversal
    TODO    Complete documentation
    
    TODO    Implement   logging functionality.
    TODO    Implement   unit tests.
    """
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.left: BinarySearchTreeNode = None
        self.right: BinarySearchTreeNode = None
    
    def insert_child(self, data: Any) -> None:
        """_summary_

        Parameters
        ----------
        data : Any
            _description_
        """
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.insert_child(data=data)
                return
            else:
                self.left = BinarySearchTreeNode(data=data)
                return
        if self.right:
            self.right.insert_child(data=data)
            return
        else:
            self.right = BinarySearchTreeNode(data=data)
            return
    
    def in_order_traversal(self) -> list:
        """
        First visit the left sub-Tree, then return to the base node and visit the right sub-Tree.

        Returns
        -------
        list
            Sorted data
        """
        elements: list = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def search(self, data: Any) -> bool:
        """_summary_

        Parameters
        ----------
        data : Any
            _description_

        Returns
        -------
        bool
            _description_
        """
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data=data)
            return False
        if self.right:
            return self.right.search(data=data)
        return False
    
    def minimum(self) -> Any:
        """
        Finds minimum element in entire binary tree.

        Returns
        -------
        Any
            Minimum element in the binary tree
        """
        if self.left:
            return self.left.minimum()
        return self.data
    
    def maximum(self) -> Any:
        """
        Finds maximum element in entire binary tree.

        Returns
        -------
        Any
            Maximum element in the binary tree
        """
        if self.right:
            return self.right.maximum()
        return self.data
    
    def sum(self) -> Any:
        """
        Sum of all elements.

        Returns
        -------
        Any
            Sum of all elements
        """
        result: Any = self.data
        if self.left:
            result += self.left.sum()
        if self.right:
            result += self.right.sum()
        return result
    
    def post_order_traversal(self) -> list:
        """
        Performs post-order traversal of a binary tree

        Returns
        -------
        list
            Elements of the binary tree in post-order
        """
    
    def pre_order_traversal(self) -> list: 
        """
        Performs pre-order traversal of a binary tree

        Returns
        -------
        list
            Elements of the binary tree in pre-order
        """
    
    def delete(self, data: Any):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            #min_data = self.right.minimum()
            #self.data = min_data
            #self.right = self.right.delete(min_data)
            max_data = self.left.maximum()
            self.data = max_data
            self.left = self.left.delete(max_data)

        return self
    

def build_tree(iterable: Iterable) -> BinarySearchTreeNode:
    f"""
    Creates a binary tree with the following elements: {iterable}

    Parameters
    ----------
    iterable : Iterable
        A collection of elements

    Returns
    -------
    BinarySearchTreeNode
        The root of the binary tree
    """
    root: BinarySearchTreeNode = BinarySearchTreeNode(iterable[0])
    for element in iterable[1:]:
        root.insert_child(element)
    return root


if __name__ == '__main__':
    numbers: list[int] = [randint(1, 100) for _ in range(10)]
    print(f"{numbers=}")
    numbers_tree: BinarySearchTreeNode = build_tree(iterable=numbers)
    print(f"{numbers_tree.in_order_traversal()=}")
    print(f"{numbers_tree.search(data=numbers[0])=}")
    print(f"{numbers_tree.search(data=1_000)=}")
    print(f"{numbers_tree.search(data=10_000)=}")
    print(f"{numbers_tree.search(data=numbers[-1])=}")
    print(f"{numbers_tree.minimum()=}")
    print(f"{numbers_tree.maximum()=}")
    print(f"{numbers_tree.sum()=}")
    print(f"{numbers_tree.delete(data=numbers[0]).in_order_traversal()=}")
    print(f"{numbers_tree.delete(data=numbers[-1]).in_order_traversal()=}")
    
    names: list[str] = ["Michalis", "Moraki", "Tina", "Shiushin", "Harris", "Vicky", "Sarantis"]
    print(f"{names=}")
    names_tree: BinarySearchTreeNode = build_tree(iterable=names)
    print(f"{names_tree.in_order_traversal()=}")
    print(f"{names_tree.search(data='Michali')=}")
    print(f"{names_tree.search(data='Michalis')=}")
    print(f"{names_tree.search(data='Moraki')=}")
    print(f"{names_tree.search(data='Tina')=}")
    print(f"{names_tree.search(data='Shiushin')=}")
    print(f"{names_tree.search(data='Harris')=}")
    print(f"{names_tree.search(data='Vicky')=}")
    print(f"{names_tree.search(data='Sarantis')=}")
    print(f"{names_tree.search(data='Reina')=}")
    print(f"{names_tree.minimum()=}")
    print(f"{names_tree.maximum()=}")
    print(f"{names_tree.sum()=}")
    print(f"{names_tree.delete(data=names[0]).in_order_traversal()=}")
    print(f"{names_tree.delete(data=names[-1]).in_order_traversal()=}")
    