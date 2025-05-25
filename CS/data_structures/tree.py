from collections import deque

from node import TreeNode

"""
TODO    Implement self.is_branch
TODO    Implement self.is_leaf
TODO    Implement self.length
TODO    Implement self.number_of_nodes
"""

class Tree:
    """
    A Tree class representation.
    """
    def __init__(self, root: TreeNode = None) -> None:
        self.root: TreeNode = root
        self.length: int = 1
        self.number_of_nodes: int = 1
        self.is_branch: bool = False
        self.is_leaf: bool = True
    
    def expand(self, child: TreeNode = None) -> None:
        """_summary_

        Parameters
        ----------
        node : TreeNode
            _description_
        """
        self.root.add_child(child=child)
    
    def show(self, depth: int = None) -> None:
        """_summary_

        Parameters
        ----------
        depth : int, optional
            _description_, by default 0
        """
        self.root.show(depth=depth)
    
    def depth_first_search(self, node: TreeNode = None) -> None:
        """_summary_

        Parameters
        ----------
        node : TreeNode, optional
            _description_, by default None
        """
        self.root.depth_first_search(node=node)
    
    def breadth_first_search(self, node: TreeNode = None) -> None:
        """_summary_

        Parameters
        ----------
        node : TreeNode, optional
            _description_, by default None
        """
        self.root.breadth_first_search(node=node)
    
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
        return self.root.it_has(data=data, node=node)


if __name__ == "__main__":
    root = TreeNode(data='Electronics')
    tree: Tree = Tree(root=root)
    laptop = TreeNode(data='Laptop')
    cellphone = TreeNode(data='Cellphone')
    tv = TreeNode(data='TV')
    tree.expand(child=laptop)
    tree.expand(child=cellphone)
    tree.expand(child=tv)
    for level in range(3):
        print(f"\n----- {level=} -----")
        tree.show(depth=level)
    tree.depth_first_search()
    tree.breadth_first_search()
    print(f"{tree.it_has(data='LG')=}")
    print(f"{tree.it_has(data='LGI')=}")
    
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
        tree.show(depth=level)
    tree.depth_first_search()
    tree.breadth_first_search()
    print(f"{tree.it_has(data='LG')=}")
    print(f"{tree.it_has(data='LGI')=}")